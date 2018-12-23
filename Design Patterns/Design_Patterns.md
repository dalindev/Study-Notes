# Types of Design Patterns

As per the design pattern reference book [Design Patterns - Elements of Reusable Object-Oriented Software](https://github.com/dalinhuang99/Study-Notes/blob/master/books/Erich%20Gamma%2C%20Richard%20Helm%2C%20Ralph%20Johnson%2C%20John%20M.%20Vlissides-Design%20Patterns_%20Elements%20of%20Reusable%20Object-Oriented%20Software%20%20-Addison-Wesley%20Professional%20(1994).pdf) , there are 23 design patterns which can be classified in three categories:
* <b>Creational</b>
   * These design patterns provide a way to create objects while hiding the creation logic, rather than instantiating objects directly using new operator. This gives program more flexibility in deciding which objects need to be created for a given use case.
* <b>Structural</b>
  * These design patterns concern class and object composition. Concept of inheritance is used to compose interfaces and define ways to compose objects to obtain new functionalities.
* <b>Behavioral patterns</b>
  * These design patterns are specifically concerned with communication between objects.

# Design Principles
These authors are collectively known as Gang of Four (GOF). According to these authors design patterns are primarily based on the following principles of object orientated design.

* Program to an interface not an implementation
* Favor object composition over inheritance

Also:
* The Open/Close Principle
* Principle of Least Knowledge
* Dependency Inversion
* Hollywood Principle

# Design Patterns

### Creational Patterns
> "How should objects be created"
* Factory
* Abstract Factory
* Singleton
* Builder
* Prototype
* Dependency Injection


### Structural Patterns
> "How should classes behave and interact with each other?"
*   <details>
    <summary>Decorator</summary>
    <ul>
    <li>When to use?
    <ul>
    <li>When a class is constantly being modified to implement new interfaces</li>
    </ul>
    </li>
    <li>Decorators should be independent of each other</li>
    <li>Use the decorator pattern when you have lots of objects each with a specific behavior independent of all others</li>
    <li>For example, use decorator to check specific user role before the end point method can be used</i></li>
    <ul>
    </details>
* Adapter
* Facade
* Composite
* Flyweight
* Bridge
* Proxy


### Behavioral Patterns
> "How should objects behave and interact with each other?"
*   <details>
    <summary>Strategy</summary>
    <ul>
    <li>Make it easy to vary the behavior of a class at runtime, and do so using composition rather than inheritance</li>
    <li>Composition="has-a", Inheritance="Is-a"</li>
    <li>For example, <b>passport.js</b> has local or google strategies and you can add more.<br>
    <i>Applications can choose which strategies to employ, without creating unnecessary dependencies.</i></li>
    <ul>
    </details>

* Template
* Iterator
* Command
* Chain of Responsibility
* Memento
* Visitor State
* Mediator
* Observer

### Concurrency Patterns
> "How should a specific situation be handled under multi-threading?"


### Sources
[Software design pattern (Wikipedia)](https://en.wikipedia.org/wiki/Software_design_pattern)
[Design Patterns (www.tutorialspoint.com)](https://www.tutorialspoint.com/design_pattern/index.htm)
[Design Patterns Questions and Answers](https://www.tutorialspoint.com/design_pattern/design_pattern_questions_answers.htm)
[Design Pattern - Interview Questions](https://www.tutorialspoint.com/design_pattern/design_pattern_interview_questions.htm)