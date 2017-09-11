import poplib, sys, getpass, datetime, zipfile
from tqdm import tqdm

user, pasw = None, None

def GetM():
    global user, pasw
    M = poplib.POP3('pop.onetel.com')
    if user==None:
        user = getpass.getpass("Username: ")
    if pasw==None:
        pasw = getpass.getpass("Password: ")
    M.user( user )
    M.pass_( pasw )
    return M

print("Stat: {}".format(GetM().stat()))
if not ("y" in raw_input("Delete? (y) ")): sys.exit(0)

N = int( raw_input("Messages per iter? ") )
Q = int( raw_input("How many iterations? "))
for q in range(Q):
    now = datetime.datetime.now()
    now = now.strftime("retr-%y-%m-%d_%H-%M-%S.zip")
    # print(now)
    zf = zipfile.ZipFile(now, "w")
    
    M = GetM()
    N = min(N, M.stat()[0])
    print(N)
    for i in tqdm(range(1, N+1)):
        msg = "\n".join( [str(j) for j in M.retr(i)[1]] )
        zf.writestr( "{:06d}".format(i), msg )
 
    for i in tqdm(range(1, N+1)):
        M.dele(i)

    M.quit()
