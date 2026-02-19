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
        hash_value=hashlib.sha1(str.encode(password)).hexdigest()
        return hash_value
    
def main():
    get_hash=input("Enter the hash for which u want to get password: ")
    hash_type=lengthofhash(get_hash)
    with open("file1.txt","r") as f:
        for password in f:
            data=password[:-1]
            data_hash=conversion(data,hash_type)
            if(data_hash==get_hash):
                print(f'Password is {data}')
                break
if __name__ =="__main__":
    main()

