def route_request(user_type):
    # เลียนแบบ Logic ของ FastAPI ว่าจะ Route ไป Service ไหน
    if user_type == 'EMPLOYER':
        return 1 # ไป Service A (Reg)
    elif user_type == 'INSURED':
        return 2 # ไป Service B (Contrib) หรือ C (Benefits)
    elif user_type == 'STAFF':
        return 4 # ไป Service D (Accounting)
    elif user_type == 'STAFF':
        return 5 # ไป Service D (Accounting)
    return 1