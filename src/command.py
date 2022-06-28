from model import TrieTree


def command():
    tree = TrieTree()

    print("\n\t\t\t\t\t\tWelcom to our \"AUTO-COMPLETE AND AUTO-SUGGEST\"\n")

    while True:
        print("\n\tyour option here: ")
        print("\t\t1) Add one sentence to Trie Tree")
        print("\t\t2) Delete one sentence from Trie Tree")
        print("\t\t3) Search for a sentence in Trie Tree")
        print("\t\t4) Auto complete for your sentence")
        print("\t\t5) Say good bay :)")

        str = input("\n\t\t-->")

        match str:
            case "1":
                tree.insert_sentence(input("input your sentence: "))
            case "2":
                tree.delete(input("input your sentence: "))
            case "3":
                tree.search(input("input your sentence: "))
            case "4":
                tree.auto_complete(input("input your sentence: "))
            case "5":
                print("\n\n\t\t\t\tThank you ......we hope you come back soon\n")
                return
            case _:
                pass