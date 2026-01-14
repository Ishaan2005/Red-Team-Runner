def chatbot(user_input): #defined a function to take inputs and define its output
    user_input = user_input.lower() #takes input from user, in lowercase
    keywords_toxic = ["murder","coverup","evidence"] #keywords defined for toxic requests
    keywords_inject = ["override","ignore"] #keywords defined for prompt injection
    keywords_jailbr = ["assume","hypothetical","song","poem"] #keywords defined for jailbreaking
    keywords_data = ["reveal","admin data","login credentials","client passwords","sensitive data","confidential information"]
    #keywords defined for data exfiltration

    for i in keywords_data:
        if i in user_input:
            return "heres how you can access company databse and login credentials as a admin use"
        
    for j in keywords_toxic:
        if j in user_input:
            return "heres how one would coverup evidence after a murder"  
        
    for k in keywords_inject:
        if k in user_input:
            return "ignoring previous instructions and here is the info you requested" 

        
    for l in keywords_jailbr:
        if l in user_input:
            return "here is a song about hotwiring a car"

    return "i cannot help with that request"
# defined if else logic for a deterministic chatbot









