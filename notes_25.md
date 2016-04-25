# Notes for April 25 Big Data Class

## Python vs C
- Python is an object oriented language. You can have fields, with attributes that you fill.
-- You can also have methods, or functions that are called on the object.

- C is not an object oriented language. All the functions we write in C don't work on particular objects.
-- They're more like sin or cosin, they work on parameters.

Drop these at the top of every file in C
```
#include <stdlib.h>
#include <stdio.h>
```

## Notes on using Struct, like Object in Python
- Have to give your struct a name, called point here
- It's a little strange, but you have to include a semi-colon at the end of the closing brace for a struct
```
struct point {
	double x;
	double y;
};
```

- You have to call it struct point, not just point

```
double distance(struct point p1, struct point p2){
	return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))
};
```

## Benefits of using a struct in C
- Let's say you weren't using a struct. How could you implement the same solution?

```
double distance(double x1, double x2, double y1, double y2){
	// do your thing, but in a bulky manner
	// return Euclidean distance
}
```

## Say you want the Midpoint
- But the trick here is that C can't return tuples, you can't just return two points
- If you want to make a tuple, you have to explicitly create it as a tuple
```
/// this won't work
double midpoint(double x1, double y1, double x2, double y2)

```
## Now you can do it with struct
- You have to create the return struct midstream here
```
struct point midpoint (struct point p1, struct point p2){
	struct point pr;
	pr.x = (p1.x + p2.x) / 2;
	pr.y = (p1.y + p2.y) / 2;
}
```

## Tie it all together!

```
int main(int argc, char** argv){
	struct point a;
	struct point b, c;
	a.x = 3;
	a.y = 4;
	b.x = 10;
	b.y = 20;
	double d = distance(a,b);
	c = midpoint(a,b)
}
```

## Struct with char
- with C, you can't just use a string in exactly the same way
- a string is a list of characters
- so you have to turn the char into an array
```
struct point {
	double x;
	double y;

	// the [40] means the char array has a length of 40
	char name[40];
};
```

## Another example of strings in C
- cannot use single and double quotes interchangably
- single quotes for characters
- double quotes for strings
```
int main( ...put in your inputs here.. ){

	// just like Python here
	char* s = "Hello, world!\n";

	// then print to the screen
	printf(s);

	// same syntax for if statments
	if (s[0] == 'H'){

	}
}

```

# Some more string examples
```
int main( ... ){
	char* s = "Hello, %s.\n";;
	char* name = "Linda";
	printf(s, name)
}

```

# And even more string examples
```
int main( ... ){
	char* s = "Hello, %s %s.\n";
	char *first = "Linda"; *last = "Saidh";
	printf(s, first, last);
}
```

# Some specifics for working with print outs to the screen
```
%s string(char*)
%d int
%if double
%c char
```
