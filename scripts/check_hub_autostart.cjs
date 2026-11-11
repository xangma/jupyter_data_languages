// Exercise the actual injected script across server rendering and hydration.
const assert = require('node:assert/strict');
const {execFileSync} = require('node:child_process');
const path = require('node:path');
const vm = require('node:vm');
const data = JSON.parse(execFileSync('python3', ['-c',
  'import importlib.util,json,sys; s=importlib.util.spec_from_file_location("links",sys.argv[1]); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); print(json.dumps({"html":m.injected_script({}),"release":m.RELEASE_ID}))',
  path.join(__dirname, 'inject_jupyterhub_launch_links.py')], {encoding:'utf8'}));
const code = data.html.match(/<script id="cpd-jupyterhub-launch-links">([\s\S]*?)<\/script>/)[1];
let url = new URL(`https://example.test/python-phd/catalogue/?course-version=${data.release}&thebe=1&phd-python-thebe-ready=1`);
const pendingKey = 'phd-python-thebe-launch-pending';
const storage = new Map([[pendingKey, url.pathname + url.search]]);
const timers = [], listeners = {};
let hydrated = false, clicks = 0, reactClicks = 0;
const button = {
  dataset:{}, textContent:'', classList:{add(){}},
  getAttribute(k){return k === 'aria-label' ? 'start compute environment' : null},
  setAttribute(){}, removeAttribute(){},
  addEventListener(_, fn){this.guard = fn},
  click(){
    clicks++;
    let stopped = false;
    this.guard({preventDefault(){}, stopImmediatePropagation(){stopped=true}});
    if (!stopped && hydrated) reactClicks++;
  },
};
const location = {
  get href(){return url.href}, get origin(){return url.origin},
  get pathname(){return url.pathname}, get search(){return url.search},
  get hash(){return url.hash}, replace(){throw Error('Unexpected redirect')},
};
const later = (fn, delay=0) => {timers.push({fn,delay});};
const window = {
  location, setTimeout:later, setInterval(){},
  requestIdleCallback(fn){fn()},
  addEventListener(name,fn){listeners[name]=fn},
};
const context = {
  window, URL, URLSearchParams, Node:class {}, console,
  document:{readyState:'loading', addEventListener(){}, contains(){return true},
    querySelectorAll(selector){return selector === 'button' ? [button] : []}},
  sessionStorage:{getItem:k=>storage.get(k),removeItem:k=>storage.delete(k)},
  history:{state:{},pushState(){},replaceState(_,__,value){url=new URL(value,url)}},
  setTimeout:later, requestAnimationFrame(fn){fn()},
  MutationObserver:class {observe(){}},
  fetch:async()=>({ok:true,json:async()=>({connected:false})}),
};
vm.runInNewContext(code, context);
while(timers.length) timers.shift().fn();
assert.equal(clicks,0,'Do not consume launch intent or click before hydration');
assert.ok(storage.has(pendingKey),'Keep launch intent until the page is ready');
hydrated = true;
listeners.load();
while(timers.length) timers.shift().fn();
assert.equal(reactClicks,1,'Launch once after hydration, including an already guarded SSR button');
assert.equal(storage.has(pendingKey),false,'Consume the intent once');
console.log('PASS: cold-return auto-start waits for hydration and reaches the compute handler once');
