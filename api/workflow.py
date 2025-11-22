from nodes import GraphState, process_message, send_whatsapp_message
from langgraph.graph import StateGraph, END

def create_graph():
    """
    Create graph
    """
    workflow = StateGraph(GraphState)
    
    workflow.add_node("process", process_message)
    workflow.add_node("send_whatsapp_message", send_whatsapp_message)
    
    workflow.set_entry_point("process")
    workflow.add_edge("process", "send_whatsapp_message")
    workflow.add_edge("send_whatsapp_message", END)
    
    
    return workflow.compile()