from twisted.protocols.ftp import FTPFactory, FTPRealm
from twisted.cred.portal import Portal
from twisted.cred.checkers import AllowAnonymousAccess
from twisted.conch.checkers import SSHPublicKeyDatabase
from twisted.internet import reactor
from twisted.python.filepath import FilePath


class _CustomPublicKeyChecker(SSHPublicKeyDatabase):

    def getAuthorizedKeysFiles(self, credentials):
        print 'stuff'
        files = super(CustomPublicKeyChecker, self).getAuthorizedKeysFiles(credentials)

        pwent = self._userdb.getpwnam(credentials.username)
        path = FilePath(pwent.pw_dir).child('.ssh')
        files.append(path.child('stuff'))
        return files


p = Portal(
    FTPRealm('./'),
    [AllowAnonymousAccess()]
)

f = FTPFactory(p)

reactor.listenTCP(9876, f)
reactor.run()

