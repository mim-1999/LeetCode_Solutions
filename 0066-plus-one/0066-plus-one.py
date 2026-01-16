class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        converted_array = int("".join(map(str, digits)))
        converted_array += 1

        return [int(d) for d in str(converted_array)]


        