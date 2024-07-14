class Solution:
    def countOfAtoms(self, formula: str) -> str:
        opening_closing = {}  
        st = []  
        for i, char in enumerate(formula):
            if char == '(':
                st.append(i)
            elif char == ')':
                opening_closing[st.pop()] = i


        def countElements(start, end):
            elements = {}  # dictionary to store the count of each element
            curr_elem = ''  # current element being parsed
            quantor = ''  # quantity of the current element
            recursive_elems = {}  # elements within a nested sub-formula
            i = start

            while i <= end:
                token = formula[i] if i != end else '_'
                i += 1
                if token.isdigit():
                    quantor += token
                else:
                    if token.islower():
                        curr_elem += token
                        continue
                    if quantor:
                        quantor = int(quantor)
                    else:
                        quantor = 1
                    if recursive_elems:
                        for elem in recursive_elems:
                            recursive_elems[elem] *= quantor
                            if elem in elements:
                                elements[elem] += recursive_elems[elem]
                            else:
                                elements[elem] = recursive_elems[elem]
                        recursive_elems = {}
                    elif curr_elem:
                        if curr_elem in elements:
                            elements[curr_elem] += quantor
                        else:
                            elements[curr_elem] = quantor
                    quantor = ''

                if token.isupper():
                    curr_elem = token
                    continue

                if token == '(':
                    recursive_elems = countElements(i, opening_closing[i-1])
                    i = opening_closing[i-1] + 1
            return elements

        res = countElements(0, len(formula))
        s = ''
        for elem, amount in sorted(res.items()):
            s += elem
            if amount > 1:
                s += str(amount)
        return s