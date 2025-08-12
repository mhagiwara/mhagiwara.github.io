{"title": "Recto — a truly 2D language", "template": "page.html", "url": "recto.html", "description": "Recto is a 2D programming language that uses nested rectangles as its core syntax, encoding structure and recursion directly in space instead of a linear stream of text. Recto explores new ways to write, parse, and reason about code—and even natural language—spatially.", "image": "img/recto-cover.png"}

<style>
  img.align-left { margin-left: 0; margin-right: auto; display: block; }
</style>

# Recto — a truly 2D language

[Masato Hagiwara](/)

<p style="text-align:center">
  <img src="img/recto-cover.png"
    alt="Recto — a truly 2D language"
    style="width:50%; min-width: 280px; max-width:100%; height:auto;">
</p>
<p style="text-align:center">
  <a href="recto-pad.html#code=JTVCJTVCJTIyJTJGLSUyMiUyQyUyMiUyMiUyQyUyMiUzRCUzRCUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMi0lNUMlNUMlMjIlNUQlMkMlNUIlMjIlMjIlMkMlMjIlMkYtJTIyJTJDJTIyJTIyJTJDJTIybWF0bXVsJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyLSU1QyU1QyUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiU1RCUyQyU1QiUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyRi1tJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyLSU1QyU1QyUyMiUyQyUyMiUyMiUyQyUyMiU1RS1tJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTVFLW0lMjIlMkMlMjIlMjIlNUQlMkMlNUIlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIxJTIyJTJDJTIyJTIyJTJDJTIyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMjUlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIxNyUyMiUyQyUyMiUyMiU1RCUyQyU1QiUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMjMlMjIlMkMlMjIlMjIlMkMlMjI0JTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyNiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMjM5JTIyJTJDJTIyJTIyJTVEJTJDJTVCJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTVDJTVDLSUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMi0lMkYlMjIlMkMlMjIlMjIlMkMlMjJ2LSUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMnYtJTIyJTJDJTIyJTIyJTVEJTJDJTVCJTIyJTIyJTJDJTIyJTVDJTVDLSUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMi0lMkYlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlNUQlMkMlNUIlMjIlNUMlNUMtJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyLSUyRiUyMiU1RCU1RA==" target="_blank">
    <img src="img/recto-pad.png" class="icon">
    Open in Recto Pad
  </a>
</p>

<p>
  <a href="https://colab.research.google.com/drive/1sDgWNI-QUkamf5_kZblX9R7Vxzk7_WB7?usp=sharing" target="_blank">
    <img src="img/recto-colab.png" class="icon">
      Google Colab
    </a>
</p>


<p>
  <a href="https://github.com/mhagiwara/recto" target="_blank">
    <img src="img/recto-github.png" class="icon">
      Github
    </a>
</p>

<p>
  <a href="recto-pad.html" target="_blank">
    <img src="img/recto-pad.png" class="icon">
      Recto Pad
    </a>
</p>

## TL;DR

Recto is a 2D programming language that uses nested rectangles as its core syntax, encoding structure and recursion directly in space instead of a linear stream of text. Recto explores new ways to write, parse, and reason about code—and even natural language—spatially.

## Introduction

<p style="text-align:center">
  <img src="img/recto-hellorect.png"
    alt="Hello Recto"
    style="width:40%; min-width: 280px; max-width:100%; height:auto;">
  <a href="recto-pad.html#code=JTVCJTVCJTIyJTJGLSUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMi0lNUMlNUMlMjIlNUQlMkMlNUIlMjIlMjIlMkMlMjIlNUUtJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTVEJTJDJTVCJTIyJTIyJTJDJTIycHJpbnQlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlNUQlMkMlNUIlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlN0MtJTIyJTJDJTIycHJpbnQlMjIlMkMlMjIlMjIlMkMlMjIlNUMlMjJSZWN0byU1QyUyMiUyMiUyQyUyMi0lN0MlMjIlMkMlMjIlMjIlNUQlMkMlNUIlMjIlMjIlMkMlMjIlNUMlMjJIZWxsbyU1QyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiU1RCUyQyU1QiUyMiUyMiUyQyUyMnYtJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTVEJTJDJTVCJTIyJTVDJTVDLSUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMi0lMkYlMjIlNUQlNUQ=" target="_blank">
    <img src="img/recto-pad.png" class="icon">
    Open in Recto Pad
  </a>
</p>

Virtually all the languages we humans use—spoken, written, or artificial (such as programming languages)—are fundamentally one-dimensional. Words, phrases, and sentences are serialized into a linear sequence across time. This makes sense: language evolved from speech, where thoughts must be serialized into sound—a one-dimensional signal.

But does a language have to be one-dimensional?

<p style="text-align:center">
  <img src="img/recto-kish.jpg"
       alt="The Kish Tablet, an early example of proto-writing using pictograms to convey meaning"
       style="width:50%; min-width: 280px; max-width:100%; height:auto;">
  The Kish Tablet, an early example of proto-writing using pictograms to convey meaning (<a href="https://en.wikipedia.org/wiki/Kish_tablet">source</a>)
</p>

Long before writing, humans used spatial representations as tools for thought. As Anne-Laure Le Cunff discusses in *[Thinking in maps](https://nesslabs.com/thinking-in-maps)*, early symbolic systems like star charts in caves or medieval diagrams functioned not just as illustrations, but as visual languages for organizing meaning. From Lascaux to knowledge graphs, there’s a deep history of thinking in space—not just in time.
When you consider what truly defines a language in the modern world, only two criteria stand out:

1. **Understandable** — it must carry meaning for both humans and machines.
1. **Generable** — it must be producible by both humans and machines.

That’s it. There’s no inherent requirement that a language be linear, or pronounceable, or even textual.

In the extreme, you could imagine a futuristic “language” that works like a smartphone app: you convey what you want to express—maybe through gestures or facial expressions—and the app outputs a structured grid of emojis or icons. If both sender and receiver (human or machine) understand it, communication happens—without sound, without linearity, and without words.

There are already examples of non-1D languages out there. Sign languages, for instance, are multimodal, using facial expressions, spatial position, and hand gestures, often happening at the same time. But even they are linear in the sense that the signals unfold over time. 

<p style="text-align:center">
  <img src="img/recto-piet.gif"
       alt="Piet program that prints 'Piet'"
       style="width:25%; min-width: 140px; max-width:100%; height:auto;">
  Piet program that prints 'Piet' (<a href="https://en.wikipedia.org/wiki/Esoteric_programming_language#Piet">source</a>)
</p>

There are also esoteric programming languages like **[Befunge](https://en.wikipedia.org/wiki/Befunge)**, **[Fish](https://esolangs.org/wiki/Fish)**, and **[Piet](https://en.wikipedia.org/wiki/Esoteric_programming_language#Piet)**, that operate in two-dimensional space, typically by navigating control flow across a grid. But these systems focus more on movement through 2D space than on using it to represent meaning or structure directly. 

<table style="border-collapse:collapse; border:none;">
  <tr>
    <td style="border:none;">
      <img src="img/recto-human.jpg" alt="Human" style="width:100%; display:block; margin:auto;">
      <div style="text-align:center;">Human</div>
    </td>
    <td style="border:none;">
      <img src="img/recto-louise.jpg" alt="Louise" style="width:100%; display:block; margin:auto;">
      <div style="text-align:center;">Louise</div>
    </td>
    <td style="border:none;">
      <img src="img/recto-louise-has-question.jpg" alt="Louise has question" style="width:100%; display:block; margin:auto;">
      <div style="text-align:center;">Louise has question</div>
    </td>
  </tr>
  <tr>
    <td colspan="3" style="text-align:center; font-style:italic; border:none;">
      Examples of Heptapod B logograms from <i>Arrival</i>. (<a href="https://github.com/WolframResearch/Arrival-Movie-Live-Coding">source</a>)
    </td>
  </tr>
</table>

A more conceptual example is **[Heptapod B](https://en.wikipedia.org/wiki/Heptapod_languages)**, the fictional alien language from Arrival (based on Ted Chiang’s *Story of Your Life*), which is composed of intricate circular logograms—each representing an entire idea or sentence. Unlike linear spoken or written languages, Heptapod B is non-sequential: the whole message is laid out at once, requiring the writer to know the full content in advance.

Visual environments like **[Pure Data](https://en.wikipedia.org/wiki/Pure_Data)**, **[Max/MSP](https://en.wikipedia.org/wiki/Max_(software))**, and **[LabVIEW](https://en.wikipedia.org/wiki/LabVIEW)** use blocks and patch cables to build logic visually. While they resemble languages, these systems are often hard to read/write as languages, and lack deeper linguistic properties like structure and recursion. 

And it’s those properties—**structure** and **recursion**—that are essential to what makes a system a language in the deepest sense.

## What is Recto?

So, can we design a 2D language that still supports structure and recursion?

In one-dimensional languages, structure is expressed through phrases, clauses, and nesting—units that unfold linearly but can be composed recursively. If we step into two dimensions, we need an equivalent: a unit that can contain other elements, express relationships, and support nesting.

There are many possible candidates—any shape with an “area” could serve this role: circles, polygons, even freeform blobs. But for clarity, simplicity, and consistency, let’s choose the most straightforward option: rectangles.

Let’s call this new language **Recto**.

Recto is a programming language prototype that explores how code can live in two-dimensional space, using spatial layout not just for aesthetics, but as core syntax.

In Recto, the rectangle (or *rect*) is the core syntactic and structural unit. A rect defines a region in 2D space that can contain elements: symbols, values, or other rects. These nested rects are how Recto encodes recursive structure visually and spatially.

One immediate advantage of this approach is the natural representation of common data structures like lists, column vectors, and matrices. In conventional 1D languages, structures like matrices or tensors are typically represented using nested lists or indentation—for example:

```
tensor([[1, 2],
        [3, 4]])
```

While this works, it’s still fundamentally a linear serialization of 2D data. Recto, by contrast, treats spatial layout as a first-class part of its syntax and semantics. The 2D structure isn't just visual formatting—it’s how meaning and relationships are encoded.

This is particularly powerful in fields like linear algebra, computer graphics, and machine learning, where multi-dimensional data is fundamental.

## Grammar

Let’s get specific. Here’s what a basic rect looks like:

<p>
  <img class="align-left" src="img/recto-grammar-1.png"
    style="width:25%; min-width: 150px; max-width:100%; height:auto;">
</p>

Corners are marked as follows:

* Top-left: `/-`
* Top-right: `-\`
* Bottom-left: `\-`
* Bottom-right: `-/`

Everything inside this boundary defines the contents of the rect. Elements within a rect are separated by one or more spaces or tabs, You can place elements (e.g., `a`, `b`, `c`, etc) inside a rect. 

You can also define single-row rects (like lists or parentheses in 1D languages) using `|-` and `-|`:

<p>
  <img class="align-left" src="img/recto-grammar-2.png"
    style="width:25%; min-width: 150px; max-width:100%; height:auto;">
</p>

Or define single-column rects (like column vectors) using `^-` and `v-`:

<p>
  <img class="align-left" src="img/recto-grammar-3.png"
    style="width:80px; height:auto; ma">
</p>

A key feature of Recto is that rects can be nested. For example:

<p>
  <img class="align-left" src="img/recto-grammar-4.png"
    style="width:40%; min-width: 250px; max-width:100%; height:auto;">
</p>
<p>
  <a href="recto-pad.html#code=JTVCJTVCJTIyJTJGLSUyMiUyQyUyMiUyQiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMi0lNUMlNUMlMjIlNUQlMkMlNUIlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMkYtJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyLSU1QyU1QyUyMiUyQyUyMiUyMiUyQyUyMiUyMiU1RCUyQyU1QiUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMi0lMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlNUQlMkMlNUIlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjJjJTIyJTJDJTIyZCUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiU1RCUyQyU1QiUyMiUyMiUyQyUyMiUyMiUyQyUyMiU1QyU1Qy0lMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjItJTJGJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTVEJTJDJTVCJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTVEJTJDJTVCJTIyJTIyJTJDJTIyJTIyJTJDJTIyYSUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMmIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlNUQlMkMlNUIlMjIlNUMlNUMtJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyLSUyRiUyMiU1RCU1RA==" target="_blank">
    <img src="img/recto-pad.png" class="icon">
    Open in Recto Pad
  </a>
</p>

In this example, the inner rect `- c d` is nested inside the outer one. Recto uses **row-major order** to parse elements: that is, elements are read left-to-right within each row, and rows are read top-to-bottom.

So, this example would be parsed as:

* Inner rect: `- c d`
* Outer rect: `+ [inner rect] a b`

You can also specify the type of a rect by adding a suffix to the top-left corner:

* `/d` — Dictionary: pairs become key-value mappings
* `/s` — Set: unordered collection of elements.
* `/m` — Matrix: the spatial layout directly corresponds to rows and columns of numerical or symbolic values.

Dictionary:
<p>
  <img class="align-left" src="img/recto-grammar-d.png"
    style="width:25%; min-width: 200px; max-width:100%; height:auto;">
</p>

Set:
<p>
  <img class="align-left" src="img/recto-grammar-s.png"
    style="width:25%; min-width: 200px; max-width:100%; height:auto;">
</p>

Matrix:
<p>
  <img class="align-left" src="img/recto-grammar-m.png"
    style="width:25%; min-width: 200px; max-width:100%; height:auto;">
</p>

While `/d` (dictionary) and `/s` (set) rects often follow common visual patterns (like two columns for dictionaries), Recto does not enforce layout constraints. All elements are parsed in row-major order. It's up to the interpreter or the logic of your program to validate content or raise errors based on expected structure—not appearance.

However, `/m` (matrix) rects need to be parsed according to the internal structure (rows and columns) to determine the matrix’s dimensions.

## Parsing and Executing

Regarding parsing, in one-dimensional languages, a single stack is sufficient to handle nesting, since structure unfolds linearly and can be tracked with push and pop operations. In Recto, in addition to a row-wise stack that keeps track of rect opening and closing symbols and tokens in row-major order, you also need a column-wise stack per each column. This column-wise stack keeps track of x-axis coordinates to determine which elements belong to which rect in the presence of nested or overlapping structures.

This spatial reasoning is essential not only to resolve ownership but also to validate that a rect is well-formed (e.g., not a trapezoid or malformed box). So while there's a surface-level equivalence in how data might be serialized, the underlying structure and parsing logic are fundamentally two-dimensional.

I have written a working parser and interpreter for Recto that implements the “multi-stack” parsing approach described above. While this version defines only a limited set of grammar and features, it supports most of the core concepts outlined in this document. The source code is available on GitHub: <a href="https://github.com/mhagiwara/recto" target="_blank">📂 Recto on GitHub</a>, and you can also try it interactively in a Google Colab notebook: <a href="https://colab.research.google.com/drive/1sDgWNI-QUkamf5_kZblX9R7Vxzk7_WB7?usp=sharing" target="_blank">🚀 Try Recto in Colab</a>.

Recto’s execution model is inspired by Lisp. Function calls are evaluated by applying the first element as the function, with the remaining elements interpreted as arguments. For example, a function call looks like this:

<p>
  <img class="align-left" src="img/recto-parsing-call.png"
    style="width:20%; min-width: 150px; max-width:100%; height:auto;">
</p>

For function definitions, Recto uses the `fn` keyword, followed by the function name, parameters, and the body.

<p>
  <img class="align-left" src="img/recto-parsing-fn.png"
    style="width:35%; min-width: 200px; max-width:100%; height:auto;">
</p>

Control flow structures like `if` and `for` follow a style similar to Python. An `if` expression includes four parts: the keyword `if`, a condition, a "then" block, and an "else" block:

<p>
  <img class="align-left" src="img/recto-parsing-if.png"
    style="width:35%; min-width: 200px; max-width:100%; height:auto;">
</p>

A `for` expression consists of four elements: the keyword for, a loop variable, a range specification, and the loop body:

<p>
  <img class="align-left" src="img/recto-parsing-for.png"
    style="width:35%; min-width: 200px; max-width:100%; height:auto;">
</p>

Recto makes structured control flow visually intuitive, without relying on indentation or explicit delimiters. Instead, the 2D layout and rect boundaries define scope and grouping—just like parentheses or indentation do in traditional 1D languages, but spatially. This visual structure makes it easier to inspect large, complex logic at a glance—almost like zooming into nested blocks.

It also opens up interesting possibilities for expressing parallelism or asynchronous behavior: for example, columns could potentially represent separate threads, allowing developers to visualize concurrent logic side by side in 2D space.

More broadly, this taps into our underused capacity for spatial reasoning. Human languages and programming environments evolved from 1D media like speech and text, but visual layout—like punctuation, diagrams, or even number systems such as the [Kaktovik numerals](https://www.scientificamerican.com/article/a-number-system-invented-by-inuit-schoolchildren-will-make-its-silicon-valley-debut1/)—can dramatically improve how we communicate and compute. Just as modern punctuation unlocked clarity in writing, 2D structure might help us—and machines—see logic more clearly.

## Writing and Editing

One of the biggest challenges in making Recto practical is simply: how do you write it?

Virtually every programming tool—IDEs, version control systems, even AI assistants—is built on the assumption that code is one-dimensional. They expect text that flows from top to bottom and left to right, making authoring a 2D language like Recto awkward in current environments.

Early on, I relied on Google Sheets—manually placing symbols into cells and copying cell ranges—to represent Recto’s spatial layout. While it worked for small examples, it was tedious and not designed for coding.

<p style="text-align:center">
  <img src="img/recto-pad-screenshot.png"
    alt="Recto Pad"
    style="width:80%; max-width:100%; height:auto;">
</p>

To address this, I built a simple, interactive web tool called <strong><a href="recto-pad.html" target="_blank">Recto Pad</a></strong>. Recto Pad lets you draw the basic building blocks of Recto on a grid, including different types of rects—regular (`/-`, `-\`, `\-`, `-/`), row (`|-`, `-|`), column (`^-`, `v-`), and typed rects such as dictionaries (`/d`), sets (`/s`), and matrices (`/m`). It also supports drawing common control flow structures like `fn`, `if`, and `for`. You can import and export Recto code as plain text, which can then be fed directly into the Python interpreter. It doesn’t execute the code yet, but it makes creating and editing Recto programs far easier than working in spreadsheets.


If we were to build proper tooling for Recto, the experience would resemble design tools more than traditional code editors. Think of spatial canvases like **[Figma](https://www.figma.com/)**, **[Miro](https://miro.com/)**, or **[Muse](https://museapp.com/)**—platforms where ideas are arranged in two dimensions, not constrained by a scrolling text buffer. Writing Recto would feel more like sketching on an infinite whiteboard: spatially expressive, zoomable, and collaborative. It could enable live collaboration, visual debugging, and spatially structured code reviews—activities that are cumbersome in 1D code editors but natural in 2D environments. Projects like **[Muse](https://museapp.com/)**, **[Heptabase](https://heptabase.com/)**, and the broader “Tools for Thought” movement point to a future where visual structure becomes central to how we think, build, and communicate—not just annotate or decorate.

In some ways, this spatial paradigm is more powerful than a vertical text editor. In 1D languages, editing multiple non-adjacent parts of code at once is cumbersome. But in a 2D system like Recto, you can zoom into any subregion, rearrange elements visually, and compose complex logic without being constrained by linear flow. Even more importantly, these edits can happen in parallel—different people can work on different regions simultaneously without interfering with one another—making collaborative coding more natural and efficient.

Another open challenge is how to build AI-based coding tools for Recto. Most large language models (LLMs), which are based on the Transformer architecture, operate on linear sequences. Even models that work with visual layouts—like **[Vision Transformers](https://arxiv.org/abs/2010.11929)** (ViTs)—first flatten 2D inputs into sequences of patches, which may lose fine-grained spatial information despite using 2D positional embeddings, although sequence-based Transformer models usually generally perform well at understanding and generating 2D images.

Few autoregressive generative models natively support 2D structures, but there is promising research. Models like **[VAR](https://arxiv.org/abs/2404.02905)** and **[LayoutGPT](https://arxiv.org/abs/2305.15393)** have begun tackling generation in structured 2D spaces. These could serve as the foundation for AI assistants that understand and generate Recto code spatially, not just linearly.

## Final Words

The core idea behind Recto isn’t limited to programming—it extends naturally to natural language, especially those with flexible word order. By parsing and visually arranging phrase structures in two dimensions, Recto provides a spatial way to represent linguistic meaning.

This can be especially effective for languages like Japanese, Korean, Turkish, and Russian, where elements such as subjects, objects, and modifiers often appear in varying orders, especially around verbs. Constructed languages like **[Lojban](https://en.wikipedia.org/wiki/Lojban_grammar#Syntax_and_semantics)**, designed for logical expressiveness and syntactic flexibility, also map well to this paradigm.

Here’s an example of encoding a Japanese sentence using Recto-like 2D structure. It includes a relative clause nested inside a main clause:

<p>
  <img class="align-left" src="img/recto-nl-ja.png"
    style="width: 45%; min-width: 300px; max-width:100%; height:auto;">
</p>

<p>
  <img class="align-left" src="img/recto-nl-en.png"
    style="width:45%; min-width: 300px; max-width:100%; height:auto;">
</p>

This structure expresses:

*Yesterday at the library, Taro gave Hanako the book that Ichiro bought.*

*昨日、図書館で、太郎が花子に一郎が買った本をあげた。*

Recto is an attempt to rethink what a programming language could be—not as a linear sequence of tokens, but as something that lives in two dimensions. Instead of squeezing everything into a 1D stream, Recto lets you express structure and recursion directly in space, using rectangles.

There are still many open questions, especially around editing, parsing, and tooling, but I believe this shift in perspective—moving from 1D to 2D—can open up new ways of thinking about code, language, and meaning itself.

I’m grateful to Aza Raskin, Joshua Tanner, Sorami Shiromizu, and Keisuke Sakaguchi for their thoughtful feedback and encouragement on this project.

This work is licensed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt the material for any purpose, even commercially, as long as you give appropriate credit.

<p style="text-align:center">
  <img src="img/recto-fizzbuzz.png"
    alt="FizzBuzz in Recto"
    style="width:50%; min-width: 280px; max-width:100%; height:auto;">
  FizzBuzz in Recto <br/>
  <a href="recto-pad.html#code=JTVCJTVCJTIyJTJGLSUyMiUyQyUyMmZvciUyMiUyQyUyMm4lMjIlMkMlMjIlN0MtJTIyJTJDJTIycmFuZ2UlMjIlMkMlMjIxJTIyJTJDJTIyMjElMjIlMkMlMjItJTdDJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyLSU1QyU1QyUyMiU1RCUyQyU1QiUyMiUyMiUyQyUyMiUyRi0lMjIlMkMlMjJwcmludCUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMi0lNUMlNUMlMjIlMkMlMjIlMjIlNUQlMkMlNUIlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMkYtJTIyJTJDJTIyaWYlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlN0MtJTIyJTJDJTIyJTNEJTNEJTIyJTJDJTIyJTdDLSUyMiUyQyUyMiUyNSUyMiUyQyUyMm4lMjIlMkMlMjIxNSUyMiUyQyUyMi0lN0MlMjIlMkMlMjIwJTIyJTJDJTIyLSU3QyUyMiUyQyUyMiU1QyUyMkZpenpCdXp6JTVDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyLSU1QyU1QyUyMiUyQyUyMiUyMiUyQyUyMiUyMiU1RCUyQyU1QiUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyRi0lMjIlMkMlMjJpZiUyMiUyQyUyMiUyMiUyQyUyMiU3Qy0lMjIlMkMlMjIlM0QlM0QlMjIlMkMlMjIlN0MtJTIyJTJDJTIyJTI1JTIyJTJDJTIybiUyMiUyQyUyMjMlMjIlMkMlMjItJTdDJTIyJTJDJTIyMCUyMiUyQyUyMi0lN0MlMjIlMkMlMjIlNUMlMjJGaXp6JTVDJTIyJTIyJTJDJTIyJTIyJTJDJTIyLSU1QyU1QyUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiU1RCUyQyU1QiUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyRi0lMjIlMkMlMjJpZiUyMiUyQyUyMiU3Qy0lMjIlMkMlMjIlM0QlM0QlMjIlMkMlMjIlN0MtJTIyJTJDJTIyJTI1JTIyJTJDJTIybiUyMiUyQyUyMjUlMjIlMkMlMjItJTdDJTIyJTJDJTIyMCUyMiUyQyUyMi0lN0MlMjIlMkMlMjIlNUMlMjJCdXp6JTVDJTIyJTIyJTJDJTIyLSU1QyU1QyUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiU1RCUyQyU1QiUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMm4lMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlNUQlMkMlNUIlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlNUMlNUMtJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyLSUyRiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiU1RCUyQyU1QiUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiU1QyU1Qy0lMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjItJTJGJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTVEJTJDJTVCJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTVDJTVDLSUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMiUyMiUyQyUyMi0lMkYlMjIlMkMlMjIlMjIlMkMlMjIlMjIlNUQlMkMlNUIlMjIlMjIlMkMlMjIlNUMlNUMtJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyJTIyJTJDJTIyLSUyRiUyMiUyQyUyMiUyMiU1RCUyQyU1QiUyMiU1QyU1Qy0lMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjIlMjIlMkMlMjItJTJGJTIyJTVEJTVE" target="_blank">
    <img src="img/recto-pad.png" class="icon">
    Open in Recto Pad
  </a>
</p>
