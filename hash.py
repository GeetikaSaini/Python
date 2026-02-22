import hashlib

def typeofhash(hash):
    if(hash==256):
        return 'SHA256'
    elif(hash==128):
        return 'MD5'
    else:
        return 'SHA1' #160
def lengthofhash(hash):
    len_hash=len(hash)*4
    hashtype=typeofhash(len_hash)
    return hashtype

def conversion(password,hash_type):
    if(hash_type=='SHA256'):
        hash_value=hashlib.SHA256(str.encode(password)).hexdigest()
        return hash_value
    elif(hash_type=='MD5'):
        hash_value=hashlib.md5(str.encode(password)).hexdigest()
        return hash_value
    else:
        hash_value=hashlib.SHA1(str.encode(password)).hexdigest()
        return hash_value

def main():
    resp=input("""\nEnter what you want to do
           1)Check what is hash type
           2)Password Cracker\n""")
    print('You have selected option: ',resp)
    match resp:
        case '1':
            hash_check=input('Enter the hash you want to check: ')
            hash_type=lengthofhash(hash_check)
            print(hash_type)
        case '2':
            get_hash=input("Enter the hash for which u want to get password: ")
            hash_type=lengthofhash(get_hash)
            password=input('Enter the password: ')
            conv_hash=conversion(password,hash_type)
            if(conv_hash==get_hash):
                print("Successfull")
            else:
                print('Unsuccessfull')

if __name__ =="__main__":
    main()
