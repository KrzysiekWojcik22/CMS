import paramiko

class SFTP:
    def create_sftp_client(host, port, username, password, keyfilepath, keyfiletype):
        """
        If a private key is used for authentication, the type of the keyfile needs to be specified as DSA or RSA.
        :rtype: SFTPClient object.
        """
        sftp = None
        key = None
        transport = None
        try:
            if keyfilepath is not None:
                if keyfiletype == 'DSA':
                    key = paramiko.DSSKey.from_private_key_file(keyfilepath)
                else:
                    key = paramiko.RSAKey.from_private_key(keyfilepath)
            transport = paramiko.Transport((host, port))
            transport.connect(None, username, password, key)

            sftp = paramiko.SFTPClient.from_transport(transport)

            return sftp
        except Exception as e:
            print('An error occurred creating SFTP client: %s: %s' % (e.__class__, e))
            if sftp is not None:
                sftp.close()
            if transport is not None:
                transport.close()
            pass

