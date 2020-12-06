# Aero

### What is Aero?

Aero is a task runner made for go. It is somehow similar to Gulp.js and very flexible.

### Motivation

My motivation to do this was that I needed a cross platform alternative to Make for [XStore](https://github.com/X-Store-App).

### How to use
#### Installation

You can install Aero from the [releases page](https://github.com/X-Store-App/aero-task-runner/releases) or [build Aero yourself](#build).

#### How to use
1. Create an aeroconfig.go file in your go.mod's directory.

2. Start coding! aeroconfig.go works like Gulp. You create a function, and you export it. The default function is `default`.

#### How to export tasks?

Aero tries to find your tasks in the aeroconfig package.

#### Creating a default task

When hitting `aero` with 0 arguments, It'll try to find the `default` function.

<div id="build">

### Building

</div>

Aero uses Aero to build itself. To get started, run `aero`.

### Sample Aero configuration file
```go
package aeroconfig

import (
	"fmt"
)

func default(stop) {
	fmt.Println("Hello, world!")
	stop()
}
```