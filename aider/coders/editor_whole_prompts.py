# flake8: noqa: E501

from .wholefile_prompts import WholeFilePrompts


class EditorWholeFilePrompts(WholeFilePrompts):
    main_system = """Act as an expert software developer and content writer and make changes to content.
{lazy_prompt}
Output a copy of each file that needs changes.
"""
