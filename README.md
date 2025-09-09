# Triangle Pattern Generator
A Python program that generates three types of triangle patterns using asterisk (*) characters.

## Overview
This program creates three distinct triangle patterns:
- Lower triangular pattern
- Upper triangular pattern  
- Pyramid pattern

## Features

- Interactive input for number of rows
- Three pattern generation functions
- Clean, readable output formatting
- Simple command-line interface

## Usage

Run the program and enter the desired number of rows when prompted:

```bash
python Week1_Assignment.py
```

## Pattern Types

### Lower Triangle
Stars increase from 1 to n rows, left-aligned:
```
*
* *
* * *
* * * *
```

### Upper Triangle
Stars decrease from n to 1 rows, left-aligned:
```
* * * *
* * *
* *
*
```

### Pyramid
Stars increase from 1 to n rows, center-aligned:
```
   *
  * *
 * * *
* * * *
```

## Functions

1. print_lower_triangle(n)
2. print_upper_triangle(n)
3. print_pyramid(n)

## Example Output

```
Enter the number of rows: 4

Lower Triangle:
* 
* * 
* * * 
* * * * 

Upper Triangle:
* * * * 
* * * 
* * 
* 

Pyramid:
   * 
  * * 
 * * * 
* * * * 
```


## How It Works

**Lower Triangle**: Prints i asterisks for row i  
**Upper Triangle**: Prints (n-i+1) asterisks for row i  
**Pyramid**: Adds (n-i) spaces before printing i asterisks for row i  

## Customization

To modify patterns:
- Change the "*" character to any other symbol
- Adjust spacing by modifying the `end=" "` parameter
- Add new pattern functions following the same structure