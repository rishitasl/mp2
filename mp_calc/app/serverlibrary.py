
### mergesort


def merge(array, p, q, r, byfunc = None):
    '''
Merge
Input:
- array = sequence of integers
- p = beginning index of left array, which is also the beginning of the input sequence
- q = ending index of left array
- r = ending index of right array
Output: None, sort the array in place
Steps:
1. nleft = q - p +1 
2. nright = r - q 
3. left_array = array[p...q]
4. right_array = array[(q+1)...r]
5. left = 0
6. right = 0
7. dest = p
8. As long as (left < nleft) AND (right < nright), do:
    8.1 if left_array[left] <= right_array[right], do:
        8.1.1 array[dest] = left_array[left]
        8.1.2 left = left + 1
    8.2 otherwise, do:
        8.2.1 array[dest] = right_array[right]
        8.2.2 right = right + 1
    8.3 dest = dest + 1
9. As long as (left < nleft), do:
    9.1 array[dest] = left_array[left]
    9.2 left = left + 1
    9.3 dest = dest + 1
10. As long as (right < nright), do:
    9.1 array[dest] = right_array[right]
    9.2 right = right + 1
    9.3 dest = dest + 1'''
    if byfunc == None:
        byfunc = lambda x:x
    nleft = q - p +1 
    nright = r - q 
    left_array = array[p:q+1]
    right_array = array[q+1:r+1]
    left = 0
    right = 0
    dest = p
    while (left < nleft) and (right < nright):
        if byfunc(left_array[left]) <= byfunc(right_array[right]): # Add criteria based on byfunc
            array[dest] = left_array[left]
            left = left + 1
        else:
            array[dest] = right_array[right]
            right = right + 1
        dest += 1
    while left < nleft:
        array[dest] = left_array[left]
        left += 1
        dest += 1
    while right < nright:
        array[dest] = right_array[right]
        right += 1
        dest += 1
    return 0
    
    

def mergesort_recursive(array, p, r, byfunc = None):
    '''Merge Sort
Input: 
 - array = sequence of integers
 - p = index of beginning of array
 - r = index of end of array
Output: None, sort the array in place
Steps:
1. if r - p > 0, do:
    1.1 calculate q = (p + r) / 2
    1.2 call MergeSort(array, p, q)
    1.3 call MergeSort(array, q+1, r)
    1.4 call Merge(array, p, q, r)'''
    if r-p > 0:
        q = (p+r) // 2
        mergesort_recursive(array, p, q, byfunc)
        mergesort_recursive(array, q+1, r, byfunc)
        merge(array, p, q, r, byfunc)
    return 0

def mergesort(array, byfunc = None):
    mergesort_recursive(array, 0, len(array)-1, byfunc)
    
### End of mergesort

class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if len(self.__items) > 0:
            return self.__items.pop()
        else:
            return None

    def peek(self):
        if self.is_empty:
            return ""
        return self.__items[-1]
    
    def show(self):
        print(self.__items)

    @property
    def is_empty(self):
        return len(self.__items) == 0

    @property
    def size(self):
        return len(self.__items)



class EvaluateExpression:
    
    valid_char = '0123456789+-*/() '
    def __init__(self, string=""):
        self.expression = string

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, new_expr):
        ste = True
        for x in new_expr:
            ste *= x in self.valid_char
        if ste:
            res = new_expr
        else:
            res = ""
        self._expression = res

    def insert_space(self):
        res = ""
        ops = "+-*/()"
        for x in self.expression:
            if x in ops:
                add = " " + x + " "
            else:
                add = x
            res += add      
        return res

    def process_operator(self, operand_stack, operator_stack):
        f = {"+":lambda x,y:x+y,
             "-":lambda x,y:x-y,
             "*":lambda x,y:x*y,
             "/":lambda x,y:x//y}
        while not operator_stack.is_empty:
            right = operand_stack.pop()
            left = operand_stack.pop()
            op = operator_stack.pop()
            operand_stack.push(f[op](left,right))
    
    def process_step(self, operand_stack, operator_stack):
        f = {"+":lambda x,y:x+y,
         "-":lambda x,y:x-y,
         "*":lambda x,y:x*y,
         "/":lambda x,y:x//y}
    # while not operator_stack.is_empty:
        right = operand_stack.pop()
        left = operand_stack.pop()
        op = operator_stack.pop()
        operand_stack.push(f[op](left,right))
        
    def evaluate(self):
        ops = "+-*/()"
        operand_stack = Stack()
        operator_stack = Stack()
        expression = self.insert_space()
        tokens = expression.split()
        for x in tokens:
            # print(x)
            if x in "0123456789":
                operand_stack.push(int(x))
            elif x in "+-":
                while not operator_stack.is_empty \
                    and not operator_stack.peek() in "()":
                    self.process_step(operand_stack, operator_stack)
                operator_stack.push(x)
            elif x in "*/":
                # print(operand_stack.show())
                # print(operator_stack.show())
                while not operator_stack.is_empty \
                        and operator_stack.peek() in "*/":
                    self.process_step(operand_stack, operator_stack)
                operator_stack.push(x)
            elif x =="(":
                operator_stack.push(x)
            elif x == ")":
                while not operator_stack.is_empty:
                    if operator_stack.peek() == "(":
                        # print("banana")
                        operator_stack.pop()
                        break
                    self.process_step(operand_stack, operator_stack)
                    
        # print(operand_stack.show())
        # print(operator_stack.show())
        self.process_operator(operand_stack, operator_stack)
        return operand_stack.pop()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





