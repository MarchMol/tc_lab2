import json

# Json file readear
def read_json_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file {file_path}.")
    return data

def transition(q,a,d):
    key = "("+q+","+a+")"
    return d[key]
    
def final_state(q,w,d):
    state = q
    for a in w:
        state = transition(state,a,d)
    return state

def accepted(q,w,d,f):
    if final_state(q,w,d) in f:
        return True
    else:
        return False

def derivation(q,w,d):
    if(len(w) >0):
        state = transition(q, w[0], d)
        print(q+": "+w)
        w = w[1:]
        return derivation(state,w,d)
    else:
        return q

    
# Menu printing
def print_menu():
    print("Seleccionar funcion:")
    print("1. Transicion")
    print("2. Estado Final")
    print("3. Aceptacion")
    print("4. Derivación")
    print("5. salir")
    try:
        opt = int(input("-> "))
        if opt<1 and opt>5:
            print("Opcion invalida")
            return 0
    except:
        print("Opcion invalida")
        return 0
    return opt
    
# Switch case for options
def handle_option(opt, F, D):
    q = input("q (estado inicial): ")
    try:
        if opt==1: # Transition
            a = input("a (arista de transición): ")
            rslt = transition(q,a,D)
        if opt==2: # Final state
            w = input("w (cadena): ")
            rslt = final_state(q,w,D)
        if opt==3: # Accepted state
            w = input("w (cadena): ")
            rslt = accepted(q, w, D, F)
        if opt==4: # Derivation
            w = input("w (cadena): ")
            rslt = derivation(q,w,D)
        print("R// "+str(rslt)+"\n")
    except:
        print("Hubo un error\n")

    
def main():
    # Loading json file for the automata
    afd = input("Ingresar nombre del archivo .json para el AFD: \n")
    opt = 0
    try:
        data = read_json_file(afd)
        Q = data["Q"]
        S = data["Σ"]
        q0 = data["q0"]
        F = data["F"]
        D = data["δ"]
    except: opt=5
    
    # Menu loop
    while opt!=5:
        opt = print_menu()
        if opt!=0 and opt!=5:
            handle_option(opt, F, D)

main()
