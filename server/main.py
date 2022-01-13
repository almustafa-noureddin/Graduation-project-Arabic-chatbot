from dialog_manager import Conversation 
from intent_classifier import load_models, make_prediction, get_candidate_classes 
from preprocessing import TextCleaner 
from network_interface import create_server, start_server 
from database_interface import add_entry 
models = load_models('all') 
cleaner = TextCleaner() 
def chatbot(conv, text): 
    cand = get_candidate_classes(text, models, 'all') 
    pred, prob = make_prediction(text, models, 'all') 
    text = cleaner.transform([text])[0][0] 
    conv.set_candidates(indices=cand) 
    conv.set_user_utrance(text) 
    responce, state = conv.generate_responce() 
    if state == 'first responce': 
        add_entry(text, pred) 
    return responce, conv 
server_socket = create_server() 
start_server(server_socket, Conversation, chatbot)