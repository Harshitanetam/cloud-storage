import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

        def upload_file(self, file_From, file_to):
            dbx = dropbox.Dropbox(self.access_token)


            f = open(file_from, 'rb')
            dbx.files_upload(f.read(), file_to)

            def main():
                access_token = 'sl.AbkOy7cwlr949HZB7JxLOMrnYKuY39PSkiEnMjmzkLJ8mukldzSQjT8oLVfn_A-kByn6O0erRD07aV-9JeaGvvRpolFEVvwg3_p2AufnkjhGlCgTVtpR4YV0SKhk6nbU2-zt-ZAB'
                TransferData = TransferData(access_token)

                file_from = input("Enter the file path to transfer : -")
                file_to = input ("enter the full path to upload to dropbox:-")#this is a full path to upload file to,including name that you wish the file to be call once uploaded

                #API v2
                transferData.upload_file(file_from, file_to)
                print("file has been moved !!!")



                main()