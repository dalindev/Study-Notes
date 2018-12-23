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

>Note: ❗ == important

### Creational Patterns
> "How should objects be created"

| Name                 | Description                                                                                                                                                                                                   | Example | Important |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | :-------: |
| Abstract Factor      | Provide an interface for creating families of related or dependent objects without specifying their concrete classes                                                                                          |         |    ❗❗     |
| Builder              | Separate the construction of a complex object from its representation, allowing the same construction process to create various representations.                                                              |         |     ❗     |
| Dependency Injection | A class accepts the objects it requires from an injector instead of creating the objects directly.                                                                                                            |         |           |
| Factory method       | Define an interface for creating a single object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.                                        |         |    ❗❗     |
| Prototype            | Specify the kinds of objects to create using a prototypical instance, and create new objects from the 'skeleton' of an existing object, thus boosting performance and keeping memory footprints to a minimum. |         |     ❗     |
| Singleton            | Ensure a class has only one instance, and provide a global point of access to it.                                                                                                                             |         |    ❗❗     |


<!-- * Factory ❗❗ -->


### Structural Patterns
> "How should classes behave and interact with each other?"

| Name                            | Description                                                                                                                                                                                                                                 | Example | Important |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | :-------: |
| Adapter, Wrapper, or Translator | Convert the interface of a class into another interface clients expect. An adapter lets classes work together that could not otherwise because of incompatible interfaces. The enterprise integration pattern equivalent is the translator. |         |    ❗❗     |
| Bridge                          | Decouple an abstraction from its implementation allowing the two to vary independently.                                                                                                                                                     |         |    ❗❗     |
| Composite                       | Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.                                                                            |         |    ❗❗     |
| Decorator                       | Attach additional responsibilities to an object dynamically keeping the same interface. Decorators provide a flexible alternative to subclassing for extending functionality.                                                               |         |    ❗❗     |
| Facade                          | Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.                                                                                          |         |    ❗❗     |
| Flyweight                       | Use sharing to support large numbers of similar objects efficiently.                                                                                                                                                                        |         |     ❗     |
| Proxy                           | Provide a surrogate or placeholder for another object to control access to it.                                                                                                                                                              |         |     ❗     |


### Behavioral Patterns
> "How should objects behave and interact with each other?"

| Name                          | Description                                                                                                                                                                                                           | Example | Important |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | :-------: |
| Chain of Responsibility       | Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.    |         |    ❗❗     |
| Command                       | Encapsulate a request as an object, thereby allowing for the parameterization of clients with different requests, and the queuing or logging of requests. It also allows for the support of undoable operations.      |         |     ❗     |
| Interpreter                   | Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.                                                              |         |     ❗     |
| Iterator                      | Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.                                                                                              |         |     ❗     |
| Mediator                      | Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it allows their interaction to vary independently. |         |     ❗     |
| Memento                       | Without violating encapsulation, capture and externalize an object's internal state allowing the object to be restored to this state later.                                                                           |         |     ❗     |
| Observer or Publish/subscribe | Define a one-to-many dependency between objects where a state change in one object results in all its dependents being notified and updated automatically.                                                            |         |    ❗ ❗    |
| State                         | Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.                                                                                                    |         |     ❗     |
| Strategy                      | Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.                                                          |         |    ❗❗     |
| Template method               | Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.           |         |    ❗ ❗    |
| Visitor                       | Represent an operation to be performed on the elements of an object structure. Visitor lets a new operation be defined without changing the classes of the elements on which it operates.                             |         |     ❗     |


### Concurrency Patterns
> "How should a specific situation be handled under multi-threading?"
| Name                    | Description                                                                                                                                                                                                           | Example | Important |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | :-------: |
| Active Object           | Decouples method execution from method invocation that reside in their own thread of control. The goal is to introduce concurrency, by using asynchronous method invocation and a scheduler for handling requests.    |         |           |
| Monitor object          | An object whose methods are subject to mutual exclusion, thus preventing multiple objects from erroneously trying to use it at the same time.                                                                         |         |           |
| Reactor                 | A reactor object provides an asynchronous interface to resources that must be handled synchronously.                                                                                                                  |         |           |
| Scheduler               | Explicitly control when threads may execute single-threaded code.                                                                                                                                                     |         |           |
| Thread pool             | A number of threads are created to perform a number of tasks, which are usually organized in a queue. Typically, there are many more tasks than threads. Can be considered a special case of the object pool pattern. |         |           |
| Thread-specific storage | Static or "global" memory local to a thread.                                                                                                                                                                          |         |           |


### Model–View–Controller Pattern
> Model–view–controller is an architectural pattern commonly used for developing user interfaces that divides an application into three interconnected parts. This is done to separate internal representations of information from the ways information is presented to and accepted from the user.[1][2] The MVC design pattern decouples these major components allowing for efficient code reuse and parallel development.


### Sources
[Software design pattern (Wikipedia)](https://en.wikipedia.org/wiki/Software_design_pattern)
[Design Patterns (www.tutorialspoint.com)](https://www.tutorialspoint.com/design_pattern/index.htm)
[Design Patterns Questions and Answers](https://www.tutorialspoint.com/design_pattern/design_pattern_questions_answers.htm)
[Design Pattern - Interview Questions](https://www.tutorialspoint.com/design_pattern/design_pattern_interview_questions.htm)`


### Criticism
Inappropriate use of patterns may unnecessarily increase complexity
