def evaluate_expression(expression):
    def helper(index): #Define a helper function to recursively evaluate the expression
        result = '' # Initialize the result variable to store after evaluation
        num = 0  # Initialize the variable to store the multiplier for repetition
        while index < len(expression): #loop through each char
            char = expression[index] #get the current char
            if char.isalpha():
                result += char #if char is alphabet, add to result
            elif char.isdigit():
                num = num * 10 + int(char) #if the char is digit, update the multiplier
            elif char == '(':
                sub_result, index = helper(index + 1) #if char is parenthesis, then recursively evaluate
                result += num * sub_result #add the evaluated expression inside () to the result
                num = 0 #reset multiplier
            elif char == ')':
                return result, index #if char is ')' retrun result and index
            else:
                raise ValueError("Error: Invalid Character!") #raise Error if the char is invalid
            index += 1
        return result, index

    return helper(0)[0]  # Call the helper function with initial index 0 and return the result

def validate_expression(expression):
    opening_count = expression.count('(')  # Count the number of opening parentheses
    closing_count = expression.count(')')  # Count the number of closing parentheses
    if opening_count != closing_count:   # If the counts are not equal
        return False          # The expression is invalid
    if expression.find('(') > expression.find(')'):  # If closing parenthesis appears before opening parenthesis
        return False   # The expression is invalid
    return True        # Otherwise, the expression is valid                 
    ## return expression.count('(') == expression.count(')'): #if the count of '(' is not equal to ')', print invalid expression
        
    
def main():
    while True:
        expression = input("Enter the expression (':q' to exit): ")
        if expression.lower() == ':q':
            print("Quiting...")
            break #if the User wants to Quit, inform the user and exit the loop
        if not validate_expression(expression):
            print("Error: Invalid expression! Parentheses mismatch.") #print Invalid if the expression is invalid
            continue
        try:
            result = evaluate_expression(expression) #evaluate the expression
            print("Evaluated result:", result) #print the result after evaluation
        except ValueError as e:
            print("Error:", e) #to print any error msg

if __name__ == "__main__":
    main()
