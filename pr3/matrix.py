import numpy as np
from tabulate import tabulate
from scipy.linalg import hessenberg


def mul(A, B):
    return A @ B  # или реализация ручками?


def add(A, B):
    return A + B  # аналогично...


def inverse(A):
    return np.linalg.inv(A)  # я такая же фигня


'''
QR decomposition with shifts and hessenberg for computing eigenvalues
'''


def eigen_values(A, iterations=500000):
    Ak = hessenberg(A)  # transforms matrix to lousy-triangular form
    n = Ak.shape[0]
    QQ = np.eye(n)
    for k in range(iterations):
        # s_k is the last item of the first diagonal
        s = Ak.item(n - 1, n - 1)
        smult = s * np.eye(n)
        # pe perform qr and subtract smult
        Q, R = np.linalg.qr(np.subtract(Ak, smult))
        # we add smult back in
        Ak = np.add(R @ Q, smult)
        QQ = QQ @ Q

    return Ak.diagonal()


if __name__ == '__main__':
    n = 5
    A = np.random.rand(n, n)
    print("A=")
    print(tabulate(A))
    Ak, QQ = eigen_values(A)
    print(tabulate(Ak))
    a = sorted(Ak.diagonal())
    b = np.linalg.eigvals(A)
    b = sorted(b.astype(float))
    print(a, b, np.allclose(a, b))  # approximate test with actual values
