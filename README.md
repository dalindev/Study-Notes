# Study Notes
---
(TODO put into different categories)

### TODO list
* CURL
* HTTP 2.0 (Bidirectional) https://http2.github.io/faq/
  - HPACK Header compression
  - Server-side resource pushing
  - Multiplexing via streams and frames
  - Client/server prioritization
* HTTPS
* Socket
* SSL / OpenSSL
* Web Latency
* TCP
* UDP
* IP
* (QUIC protocol)
* Microservices https://www.youtube.com/watch?v=CZ3wIuvmHeM


### ONGOING list
Redis:
https://www.youtube.com/watch?v=Hbt56gFj998
https://www.youtube.com/watch?v=9S-mphgE5fA


### Completed.
* HTTP 
* REST - exposes Resources which represent DATA
* SOAP - exposes Operations which represent Logic
* A/B testing https://vwo.com/ab-testing/


### The JavaScript language
<details>
  <summary>
    Show details
  </summary>
  
```javascript
// get content as markdown format from this page https://javascript.info/
const textContent = (Object.values(document.querySelectorAll('.list__item'))).map( (e) => {
  let out = `##### ${e.querySelector('.list__link').textContent} \n`;
  e.querySelectorAll('.list-sub__link').forEach( (sub) => {
    out += `* [${sub.textContent}](${sub.href}) \n`;
  });
  return out;
});
console.log(textContent.toString());
```
<details>
  <summary>
    Show details
  </summary>
  
##### An introduction
* [An Introduction to JavaScript](https://javascript.info/intro)
* [Code editors](https://javascript.info/code-editors)
* [Developer console](https://javascript.info/devtools)
##### JavaScript Fundamentals
* [Hello, world!](https://javascript.info/hello-world)
* [Code structure](https://javascript.info/structure)
* [The modern mode, "use strict"](https://javascript.info/strict-mode)
* [Variables](https://javascript.info/variables)
* [Data types](https://javascript.info/types)
* [Type Conversions](https://javascript.info/type-conversions)
* [Operators](https://javascript.info/operators)
* [Comparisons](https://javascript.info/comparison)
* [Interaction: alert, prompt, confirm](https://javascript.info/alert-prompt-confirm)
* [Conditional operators: if, '?'](https://javascript.info/ifelse)
* [Logical operators](https://javascript.info/logical-operators)
* [Loops: while and for](https://javascript.info/while-for)
* [The "switch" statement](https://javascript.info/switch)
* [Functions](https://javascript.info/function-basics)
* [Function expressions and arrows](https://javascript.info/function-expressions-arrows)
* [JavaScript specials](https://javascript.info/javascript-specials)
##### Code quality
* [Debugging in Chrome](https://javascript.info/debugging-chrome)
* [Coding style](https://javascript.info/coding-style)
* [Comments](https://javascript.info/comments)
* [Ninja code](https://javascript.info/ninja-code)
* [Automated testing with mocha](https://javascript.info/testing-mocha)
* [Polyfills](https://javascript.info/polyfills)
##### Objects: the basics
* [Objects](https://javascript.info/object)
* [Garbage collection](https://javascript.info/garbage-collection)
* [Symbol type](https://javascript.info/symbol)
* [Object methods, "this"](https://javascript.info/object-methods)
* [Object to primitive conversion](https://javascript.info/object-toprimitive)
* [Constructor, operator "new"](https://javascript.info/constructor-new)
##### Data types
* [Methods of primitives](https://javascript.info/primitives-methods)
* [Numbers](https://javascript.info/number)
* [Strings](https://javascript.info/string)
* [Arrays](https://javascript.info/array)
* [Array methods](https://javascript.info/array-methods)
* [Iterables](https://javascript.info/iterable)
* [Map, Set, WeakMap and WeakSet](https://javascript.info/map-set-weakmap-weakset)
* [Object.keys, values, entries](https://javascript.info/keys-values-entries)
* [Destructuring assignment](https://javascript.info/destructuring-assignment)
* [Date and time](https://javascript.info/date)
* [JSON methods, toJSON](https://javascript.info/json)
##### Advanced working with functions
* [Recursion and stack](https://javascript.info/recursion)
* [Rest parameters and spread operator](https://javascript.info/rest-parameters-spread-operator)
* [Closure](https://javascript.info/closure)
* [The old "var"](https://javascript.info/var)
* [Global object](https://javascript.info/global-object)
* [Function object, NFE](https://javascript.info/function-object)
* [The "new Function" syntax](https://javascript.info/new-function)
* [Scheduling: setTimeout and setInterval](https://javascript.info/settimeout-setinterval)
* [Decorators and forwarding, call/apply](https://javascript.info/call-apply-decorators)
* [Function binding](https://javascript.info/bind)
* [Currying and partials](https://javascript.info/currying-partials)
* [Arrow functions revisited](https://javascript.info/arrow-functions)
##### Objects, classes, inheritance
* [Property flags and descriptors](https://javascript.info/property-descriptors)
* [Property getters and setters](https://javascript.info/property-accessors)
* [Prototypal inheritance](https://javascript.info/prototype-inheritance)
* [F.prototype](https://javascript.info/function-prototype)
* [Native prototypes](https://javascript.info/native-prototypes)
* [Methods for prototypes](https://javascript.info/prototype-methods)
* [Class patterns](https://javascript.info/class-patterns)
* [Classes](https://javascript.info/class)
* [Class inheritance, super](https://javascript.info/class-inheritance)
* [Class checking: "instanceof"](https://javascript.info/instanceof)
* [Mixins](https://javascript.info/mixins)
##### Error handling
* [Error handling, "try..catch"](https://javascript.info/try-catch)
* [Custom errors, extending Error](https://javascript.info/custom-errors)
##### Document
* [Browser environment, specs](https://javascript.info/browser-environment)
* [DOM tree](https://javascript.info/dom-nodes)
* [Walking the DOM](https://javascript.info/dom-navigation)
* [Searching: getElement* and querySelector*](https://javascript.info/searching-elements-dom)
* [Node properties: type, tag and contents](https://javascript.info/basic-dom-node-properties)
* [Attributes and properties](https://javascript.info/dom-attributes-and-properties)
* [Modifying the document](https://javascript.info/modifying-document)
* [Styles and classes](https://javascript.info/styles-and-classes)
* [Element size and scrolling](https://javascript.info/size-and-scroll)
* [Window sizes and scrolling](https://javascript.info/size-and-scroll-window)
* [Coordinates](https://javascript.info/coordinates)
##### Introduction into Events
* [Introduction to browser events](https://javascript.info/introduction-browser-events)
* [Bubbling and capturing](https://javascript.info/bubbling-and-capturing)
* [Event delegation](https://javascript.info/event-delegation)
* [Browser default actions](https://javascript.info/default-browser-action)
* [Dispatching custom events](https://javascript.info/dispatch-events)
##### Events in details
* [Mouse events basics](https://javascript.info/mouse-events-basics)
* [Moving: mouseover/out, mouseenter/leave](https://javascript.info/mousemove-mouseover-mouseout-mouseenter-mouseleave)
* [Drag'n'Drop with mouse events](https://javascript.info/mouse-drag-and-drop)
* [Keyboard: keydown and keyup](https://javascript.info/keyboard-events)
* [Scrolling](https://javascript.info/onscroll)
* [Page lifecycle: DOMContentLoaded, load, beforeunload, unload](https://javascript.info/onload-ondomcontentloaded)
* [Resource loading: onload and onerror](https://javascript.info/onload-onerror)
##### Forms, controls
* [Form properties and methods](https://javascript.info/form-elements)
* [Focusing: focus/blur](https://javascript.info/focus-blur)
* [Events: change, input, cut, copy, paste](https://javascript.info/events-change-input)
* [Form submission: event and method submit](https://javascript.info/forms-submit)
##### Animation
* [Bezier curve](https://javascript.info/bezier-curve)
* [CSS-animations](https://javascript.info/css-animations)
* [JavaScript animations](https://javascript.info/js-animation)
##### Frames and windows
* [Popups and window methods](https://javascript.info/popup-windows)
* [Cross-window communication](https://javascript.info/cross-window-communication)
* [The clickjacking attack](https://javascript.info/clickjacking)
##### Regular expressions
* [Patterns and flags](https://javascript.info/regexp-introduction)
* [Methods of RegExp and String](https://javascript.info/regexp-methods)
* [Character classes](https://javascript.info/regexp-character-classes)
* [Escaping, special characters](https://javascript.info/regexp-escaping)
* [Sets and ranges [...]](https://javascript.info/regexp-character-sets-and-ranges)
* [The unicode flag](https://javascript.info/regexp-unicode)
* [Quantifiers +, *, ? and {n}](https://javascript.info/regexp-quantifiers)
* [Greedy and lazy quantifiers](https://javascript.info/regexp-greedy-and-lazy)
* [Capturing groups](https://javascript.info/regexp-groups)
* [Backreferences: \n and $n](https://javascript.info/regexp-backreferences)
* [Alternation (OR) |](https://javascript.info/regexp-alternation)
* [String start ^ and finish $](https://javascript.info/regexp-anchors)
* [Multiline mode, flag "m"](https://javascript.info/regexp-multiline-mode)
* [Lookahead (in progress)](https://javascript.info/regexp-lookahead)
* [Infinite backtracking problem](https://javascript.info/regexp-infinite-backtracking-problem)
##### Promises, async/await
* [Introduction: callbacks](https://javascript.info/callbacks)
* [Promise](https://javascript.info/promise-basics)
* [Promises chaining](https://javascript.info/promise-chaining)
* [Promise API](https://javascript.info/promise-api)
* [Async/await](https://javascript.info/async-await)

</details>


