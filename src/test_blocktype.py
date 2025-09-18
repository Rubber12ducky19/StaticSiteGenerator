import unittest
from blocktype import block_to_block_type, BlockType

class test_block_to_blocktype(unittest.TestCase):
    def test_blocktoblocktype(self):
        print("\nBlock to Blocktype :")
        code_test_node = """```This is a code block
         some more code
          even more code ```"""
        code_expected_result = BlockType.CODE
        print("-'Code':")
        code_result_node = block_to_block_type(code_test_node)
        self.assertEqual(code_expected_result,code_result_node,)
        print("-Passed")
        
        quote_test_node = """>This is a Quote block
>This is a second Quote Block
>Finally and Third Quote Block"""
        quote_expected_result = BlockType.QUOTE
        print("-'Quote':")
        quote_result_node = block_to_block_type(quote_test_node)
        self.assertEqual(quote_expected_result,quote_result_node,)
        print("-Passed")

        unsort_test_node = """- This is a Unsorted List
- This is the second 
- This is the third"""
        unsorted_expected_result = BlockType.UNORDERED_LIST
        print("-'Unsorted List:'")
        unsorted_result_node = block_to_block_type(unsort_test_node)
        self.assertEqual(unsorted_result_node,unsorted_expected_result,)
        print("-Passed")

        heading_test_node = "### Heading Three"
        heading_expected_result = BlockType.HEADING
        print("-'Heading(Good):'")
        heading_result_node = block_to_block_type(heading_test_node)
        self.assertEqual(heading_expected_result,heading_result_node,)
        print("-Passed")

        heading7_test_node = "####### Heading Fail"
        heading7_expected_result = BlockType.PARAGRAPH
        print("-'Heading(Bad):'")
        heading7_result_node = block_to_block_type(heading7_test_node)
        self.assertEqual(heading7_expected_result,heading7_result_node,)
        print("-Passed")

        ordered_test_node = """1. First
2. Second
3. Third"""
        ordered_expected_node = BlockType.ORDERED_LIST
        print("-'Ordered List:'")
        ordered_result_node = block_to_block_type(ordered_test_node)
        self.assertEqual(ordered_expected_node, ordered_result_node,)
        print("Passed")