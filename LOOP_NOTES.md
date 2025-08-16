# Difference Between for and while Loops

## Key Points
- **for loop**: Used when you know the number of iterations. Automatically iterates over a sequence (like a list, string, or range).  
- **while loop**: Used when the number of iterations is unknown. You must manually check and update the condition to avoid infinite loops.

## Example

**for loop**
```python
for i in range(5):
    print(i)  # prints 0,1,2,3,4 automatically


**while loop**
```python
i = 0
while i < 5:
    print(i)  # prints 0,1,2,3,4
    i += 1    # manual update
