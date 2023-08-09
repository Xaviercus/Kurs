# def powtarzanie():
#     ciag = input("znaki: ")
#     liczba = input("liczba: ")
#
#     if liczba:
#         liczba = int(liczba)
#     else:
#         liczba = 1
#
#     for i in range(liczba):
#         print(ciag)
#
# powtarzanie()

def powtarzanie(ciag, liczba = 1):

    for i in range(liczba):
        print(ciag)

powtarzanie("dasda")
powtarzanie("2222", 5)


