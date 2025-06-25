employment = {
    "reader": f"""
    "EMPLOYMENT": ['EMPLOYMENT_Employed', 'EMPLOYMENT_Unemployed', 'EMPLOYMENT_Underemployed', 'EMPLOYMENT_Retired', 'EMPLOYMENT_Student', 'EMPLOYMENT_Unknown'];
    """,

    "reader_specs": f"""
    The permissible EMPLOYMENT attributes are: ['EMPLOYMENT_Employed', 'EMPLOYMENT_Unemployed', 'EMPLOYMENT_Underemployed', 'EMPLOYMENT_Retired', 'EMPLOYMENT_Student', 'EMPLOYMENT_Unknown'].
    The attribute EMPLOYMENT_Unknown means the <<text>> does not mention information regarding the current employment status of the patient at the time of <<text>>.
    The attribute EMPLOYMENT_Employed means the <<text>> explicitly mentions that patient is employmd at the time of <<text>>.
    The attribute EMPLOYMENT_Unemployed means the <<text>> explicitly mentions that patient is not employed at the time of <<text>> e.g., out of work, jobless, laid-off, etc. This includes unemployment due to disability. 
    The attribute EMPLOYMENT_Underemployed means the <<text>> explicitly mentions that patient is under-employed at the time of <<text>> e.g., low-paying job, part-time worker etc. This includes underemployment due to disability. 
    The attribute EMPLOYMENT_Retired means the <<text>> explicitly mentions that patient is retired at the time of <<text>> e.g., inactive, retired person, pensioner, etc. 
    The attribute EMPLOYMENT_Student means the <<text>> explicitly mentions that patient is student at the time of <<text>> e.g. goes to college/university, graduate/undergraduate student, etc.
    """,
    
    "cutter": f"""
    "EMPLOYMENT": Attributes include explicit indication of employment status, e.g., unemployed, employed, underemployed, student, retired, having disability or similar status. No information about employment status indicates absence of any attributes
    """
}

housing = {
    "reader": f"""
    "HOUSING": ['HOUSING_Issue', 'HOUSING_NoIssue', 'HOUSING_Unknown'];
    """,

    "reader_specs": f"""
    The permissible HOUSING attributes are: ['HOUSING_Issue', 'HOUSING_NoIssue', 'HOUSING_Unknown'].
    The attribute HOUSING_Unknown means the <<text>> does not mention information regarding the current housing status of the patient at the time of <<text>>.
    The attribute HOUSING_Issue means that <<text>> explicitly mentions an indication of unstable, inadequate, or poor quality of housing, including homeless, undomiciled for various reasons, and financial strians for housing. e.g., homeless individuals who have a primary nighttime residence that is a supervised publicly or privately operated homeless shelter, institution, or place (e.g., a bridge).
    The attribute HOUSING_NoIssue means that <<text>> did not explicitly describe any HOUSING_Issue described above, and explicitly describes or implies sufficient and stable housing. e.g., lives with wife, lives at home or with a partner, living alone, Supportive housing (section 8 housing).
    A multi-tenant house where tenants share kitchen and bathroom facilities is still considered stable housing.
    If a patient came from or was discharged from a correctional facility or detention center, you may not infer the housing situation based on the discharge alone. 
    Notes that describe patients living in [**hospital**] is a result of de-identification, and does not mean the patient actually lives in a hospital. For these cases, the patient is considered living in HOUSING_NoIssue.
    Pay attention to the current living situation of the patient. For example, living with supportive partners even after a lost of home is still considered HOUSING_NoIssue because the patient is currently living with someone.
    You may not infer the housing situation from the patient's marital status alone. For example, separated from husband/wife, or married and have children does not imply stable or unstable housing. 
    """,
    
    "cutter": f"""
    "HOUSING": Attributes include explicit indication of housing status, e.g., living at home, living alone or with a partner, supportive housing, homeless shelter, institution or similar place (e.g., bridge). No information about housing indicates absence of any attributes
    """
}

marital = {
    "reader": f"""
    "MARITAL": ['MARITAL_Married', 'MARITAL_Partnered','MARITAL_Widowed','MARITAL_Divorced','MARITAL_OtherSingleness','MARITAL_Other','MARITAL_Unknown',];
    """,

    "reader_specs": f"""
    The permissible MARITAL attributes are: ['MARITAL_Married', 'MARITAL_Partnered','MARITAL_Widowed','MARITAL_Divorced','MARITAL_OtherSingleness','MARITAL_Other','MARITAL_Unknown',].
    The attribute MARITAL_Unknown means the <<text>> does not explicitly mention information about the marital status of the patient at the time of <<text>>.
    The attribute MARITAL_Married means that <<text>> explicitly mentions the patient is legally married to a spouse.
    The attribute MARITAL_Partnered means that <<text>> explicitly mentions the patient is in a long-term, committed relationship (e.g. cohabiting), but not legally married.
    The attribute MARITAL_Widowed means that <<text>> explicitly mentions the patient's spouse or partner has passed away.
    The attribute MARITAL_Divorced means that <<text>> explicitly mentions the patient is legally divorced.
    The attribute MARITAL_OtherSingleness means that <<text>> explicitly mentions the patient is in other forms of singleness not specified in the Attributes above. e.g., never married, living alone (without mention of a previous spouse/partner).
    The attribute MARITAL_Other means that <<text>> explicitly mentions a martial status of the patient that cannot be attributed to any of the Attributes above.
    """,
    
    "cutter": f"""
    "MARITAL": Attributes include explicit indication of marital status of the patient, e.g., married, partnered, widowed, divorced. No information about marital status indicates absence of any attributes
    """
}

social = {
    "reader": f"""
    "SOCIAL": ['SOCIAL_Present', 'SOCIAL_Absent', 'SOCIAL_Unknown'];
    """,

    "reader_specs": f"""
    The permissible SOCIAL attributes are: ['SOCIAL_Present', 'SOCIAL_Absent', 'SOCIAL_Unknown'].
    The attribute SOCIAL_Unknown means the <<text>> does not explicitly mention information about the social or community support available to the patient at the time of <<text>>.
    The attribute SOCIAL_Present means that <<text>> explicitly mentions the indication/presence of social/community support available to the patient at the time of <<text>> e.g., he receives direct assistance from community every now and then, his social network helps him cope with stress, community members helped him alleviate psychological distress.
    The attribute SOCIAL_Absent means that <<text>> explicitly mentions the lack/absence of social/community support available to the patient at the time of <<text>> e.g., the risk of outbreaks increased because of no community around him, he received no social support from his community while moving out, her social network contributes nothing to alleviate her emotional distress.
    """,
    
    "cutter": f"""
    "SOCIAL": Attributes include explicit indication of presence or lack/absence of social or community support available to the patient, for example, receives direct support from the community, his social network helps him cope with stress effectively, he received no social support from his community, her social network contributes nothing to alleviate her emotional distress. No information about social/community support indicates absence of any attributes
    """
}

alcohol = {
    "reader": f"""
    "ALCOHOL": ['ALCOHOL_Current', 'ALCOHOL_Past', 'ALCOHOL_Never', 'ALCOHOL_Unknown'];
    """,

    "reader_specs": f"""
    The permissible ALCOHOL attributes are: ['ALCOHOL_Current', 'ALCOHOL_Past', 'ALCOHOL_Never', 'ALCOHOL_Unknown'].
    The attribute ALCOHOL_Unknown means the <<text>> does not contain information regarding the alcohol usage of the patient at the time of <<text>> i.e., there should be no mention of alcohol consumption or non-consumption.
    The attribute ALCOHOL_Current means that <<text>> explicitly mentions the patient is a current consumer of alcohol, regardless of past consumption history. Drinking on occasion, socially, or rarely is still considered currently consuming alcohol e.g., 'drinks alcohol now a days', 'is a daily alcohol drinker'.
    The attribute ALCOHOL_Past means that <<text>> explicitly mentions the patient is not a current consumer of alcohol but has a history of consuming alcohol only in the past. e.g., 'used to drink alcohol two years back but not now', 'was a habitual alcohol drinker previously but now doesn't drink anymore'.
    The attribute ALCOHOL_Never means that <<text>> explicitly mentions the patient never consumes alcohol, neither currently nor in the past. e.g., 'never consumed alcohol', 'neven been into habitual alcohol drinking'
    You may assume polysubstance abuse involves using alcohol.
    """,
    
    "cutter": f"""
    "ALCOHOL": Attributes include explicit evidence of alcohol consumption in the present or the past, or complete non-consumption of alcohol ever in life, for example, drinks alcohol now a days, a daily alcohol drinker, used to drink alcohol two years back but not now, a habitual alcohol drinker previously but now doesn't drink anymore, never consumed alcohol, neven been into habitual alcohol drinking. No information about alcohol usage indicates absence of any attributes.
    """
}

tobacco = {
    "reader": f"""
    "TOBACCO": ['TOBACCO_Current', 'TOBACCO_Past', 'TOBACCO_Never', 'TOBACCO_Unknown'];
    """,

    "reader_specs": f"""
    The permissible TOBACCO attributes are: ['TOBACCO_Current', 'TOBACCO_Past', 'TOBACCO_Never', 'TOBACCO_Unknown'].
    The attribute TOBACCO_Unknown means the <<text>> does not contain information regarding the tobacco usage of the patient at the time of <<text>> i.e., there should be no mention of tobacco consumption or non-consumption.
    The attribute TOBACCO_Current means that <<text>> explicitly mentions the patient is a current consumer of tobacco, regardless of past consumption history. Consuming tobacco on occasion, socially, or rarely is still considered currently consuming tobacco e.g., 'consumes tobacco now a days', 'is a chain smoker' , 'only involves in passive smoking'.
    The attribute TOBACCO_Past means that <<text>> explicitly mentions the patient is not a current consumer of tobacco but has a history of consuming tobacco only in the past. e.g., 'used to be a chain smoker two years back but now completely avoids it', 'he was a heavy cigar smoker in the past but not now'.
    The attribute TOBACCO_Never means that <<text>> explicitly mentions the patient never consumes tobacco, neither currently nor in the past. e.g., 'never consumed tobacco', 'neven been into habitual smoking', 'always avoids the cigarette and cigars'
    """,
    
    "cutter": f"""
    "TOBACCO": Attributes include explicit evidence of tobacco consumption in the present or the past, or completely avoiding the use of tobacco ever in life, for example, drinks 2-3 cigarettes on daily basis, a habitual chain smoker, used to be a cigar smoker two years back but now completely avoids it, a habitual chain smoker previously but now doesn't smoke anymore, never been into cigars and cigarettes, never consumed tobacco. No information about tobacco usage indicates absence of any attributes.
    """
}

drug = {
    "reader": f"""
    "DRUG": ['DRUG_Current', 'DRUG_Past', 'DRUG_Never', 'DRUG_Unknown'];
    """,

    "reader_specs": f"""
    The permissible DRUG attributes are: ['DRUG_Current', 'DRUG_Past', 'DRUG_Never', 'DRUG_Unknown'].
    The attribute DRUG_Unknown means the <<text>> does not contain information regarding the usage of illicit drugs by the patient at the time of <<text>> i.e., there should be no mention of consuming or non-consuming illicit drugs.
    The attribute DRUG_Current means that <<text>> explicitly mentions the patient is a current consumer of illicit drugs, regardless of past consumption history. Consuming drugs on occasion, socially, or rarely is still considered currently consuming drug e.g., 'consumes drugs daily now a days', 'rarely takes drugs like after 1 or 2 months'.
    The attribute DRUG_Past means that <<text>> explicitly mentions the patient is not a current consumer of illicit drugs but has a history of consuming illicit drugs only in the past. e.g., 'used to drugs in the past but now completely avoids it', 'he was a habitual drug consumer in the past but not now'.
    The attribute DRUG_Never means that <<text>> explicitly mentions the patient never consumes illicit drugs, neither currently nor in the past. e.g., 'never consumed drugs', 'neven been into drugs', 'always avoids the drugs'
    You may assume polysubstance abuse involves using illicit drugs.
    """,
    
    "cutter": f"""
    "DRUG": Attributes include explicit evidence of drug consumption in the present or the past, or complete avoidance of the use of drugs ever in life, for example, does drugs on daily basis, a habitual drug consumer, used to do drugs two years back but now completely avoids it,he was a habitual drug consumer in the past but not now, never been into drugs, always avoids the drugs. No information about drug usage indicates absence of any attributes.
    """
}