class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
                
        spaces_count = 0
        
        for c in text:
            if c == ' ':
                spaces_count += 1
                
        if spaces_count == 0:
            return text
        
        if len(words) <= 1:
            return "".join(words) + ' ' * spaces_count
            
            
        space_width = spaces_count // (len(words) - 1)
                
        last_space_width = spaces_count % (len(words) - 1)
        
        result = ""
        for i, word in enumerate(words):
            if i != len(words) - 1:
                result += word + ' ' * space_width
            else:
                result += word
            
        result += ' ' * last_space_width
        
        return result