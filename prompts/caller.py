def get_llm_cutter_input_message(free_text, cats = [], print_prompt=False) -> list:

   # global starter
   query = f"""
   You are given a clinical note (<<text>>) from EHRs. For each of the following SBDH Categories (in double quotes), determine whether <<text>> explicitly mentions any attribute of each category without making any inference.
   """

   # add category-wise cutter tasks
   for cat in cats:
      query += f"""{cat['cutter']}"""
      
   # output specs
   query += f"""
   After determining the attributes of each category, you must consolidate info from all SBDH Categories into a ONE-word reply: "YES" if any attribute is determined for at least one Category, or "NO" if <<text>> contains no attribute info about ANY of the Categories.
   In your final response, you must return either "YES" or "NO" and nothing else.

   Focus on the status of the patient only, and NOT the status of their family members or other personnel involved in the <<text>>.

   Input: <<{free_text}>>
   Result:
   """
   
   if print_prompt:
      print('Prompted used: \n', query)

   message_text = [
      {"role":"system","content":"You are an information extract tool that follows instructions very well and is specifically trained to extract Social and Behavioral Determinants of Health (SBDH) information from clinical notes in the EHRs."},
      {"role": "user", "content": query},
   ]
   
   return message_text

def get_llm_reader_input_message(free_text, cats = [], print_prompt=False) -> list:

   # global starter
   query = f"""
   This prompt consists of two sections: "Instruction", and "Input" which contains a clinical note from EHR. 
   Your task is to follow the "Instruction" and extract from the "Input" info about Social and Behavioral Determinants of Health (SBDH).

   Section 1: Instruction
   From the double bracketed <<text>> at the end, for each of the SBDH Categories listed below, determine the SBDH Attribute value that accurately describes the status of the patient at the time of <<text>>. 
   In each section below, each SBDH Category is shown in double quote and permissible SBDH Attributes are shown in square brackets:
   """

   # add category-wise reader tasks
   for cat in cats:
      query += f"""{cat['reader']}"""

   query += "\nFurther explanations/specifications of each Attribute is provided below:\n"

   # add category-wise specs/shots
   for cat in cats:
      query += f"""{cat['reader_specs']}"""

   # output specs
   query += f"""
   You must create key-value pairs in JSON formats:
   <CATEGORY>: <estimated Attribute from the list of permissible Attribute values>,
   <CATEGORY>_evidence: < evidence extracted from <<text>> supporting the Attribute you choose >.
   """

   # global finisher
   query += f"""
   Even if the patient expresses concerns/predictions over an upcoming change in their SBDH Attribute status, you should still assign Attribute values only based on patient's status maintained at the time of <<text>>. 
   For example "She works full time at a company, but fears that she will lose her current job" is considered “EMPLOYMENT_Employed”.
   Focus on the status of the patient only, and NOT the status of their family members or other personnel involved in the <<text>>.
   Do not infer the impact of <<text>> onto the SBDH Attributes, focus on the factual information only.

   Section 2: Input
   <<{free_text}>>
   """

   if print_prompt:
      print('Prompted used: \n', query)

   message_text = [
      {"role":"system","content":"You are an information extract tool that follows instructions very well and is specifically trained to extract Social and Behavioral Determinants of Health (SBDH) information from clinical notes in the EHRs."},
      {'role': 'user', 'content': query},
   ]

   return message_text
