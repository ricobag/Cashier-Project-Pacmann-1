#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''Pembuatan kelas dan fungsi'''

class Transaction:
    transaction_counter = 0
#transaction_counter digunakan sebagai pencatat jumlah transaksi.

    def __init__(self):
        Transaction.transaction_counter += 1
        self.transaction_id = Transaction.transaction_counter
        self.items = []
#setiap kali sebuah objek Transaction dibuat , nilai transaction_counter akan bertambah 1
#items untuk menyimpan detail item yang dibeli dalam bentuk daftar kamus.

    def add_item(self, item_name, item_quantity, item_price):
        self.items.append({
            'Item Name': item_name,
            'Quantity': item_quantity,
            'Price': item_price
        })
#fungsi ini akan membuat kamus (dictionary) baru yang mewakili item belanjaan yang akan ditambahkan ke dalam transaksi.

    def edit_item(self, item_index, item_name, item_price):
        if item_index < len(self.items):
            self.items[item_index]['Item Name'] = item_name
            self.items[item_index]['Price'] = item_price
#fungsi ini digunakan jika terdapat editing yang ingin dilakukan pada indeks item. 

    def delete_item(self, item_index):
        if item_index < len(self.items):
            del self.items[item_index]
#fungsi ini akan mengeksekusi perintah delete jika terdapat indeks item yang akan dihapus dalam transaksi

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['Quantity'] * item['Price']
        return total
#fungsi ini akan melakukan kalkulasi total belanja dan mendefinisikan items ke dalam total harga belanja

    def apply_discount(self, total):
        discount_rate = 0
        if total > 500000:
            discount_rate = 0.1
        elif total > 300000:
            discount_rate = 0.08
        elif total > 200000:
            discount_rate = 0.05
        return total - (total * discount_rate)
#fungsi ini digunakan untuk menerapkan diskon berdasarkan total belanjaan dan mengembalikan total setelah diskon

    def reset_transaction(self):
        self.items = []
#fungsi ini digunakan untuk menghapus semua item dalam transaksi (me-reset ulang)

    def display_transaction(self):
        print("Transaction ID:", self.transaction_id)
        print("Items:")
        for index, item in enumerate(self.items, 1):
            print(f"{index}. {item['Item Name']}: {item['Quantity']} x {item['Price']}")

        total = self.calculate_total()
        discounted_total = self.apply_discount(total)
        print("Total:", total)
        print("Discounted Total:", discounted_total)
#Fungsi ini digunakan untuk mencetak informasi tentang transaksi, termasuk ID transaksi, daftar item yang dibeli, total harga, dan total harga setelah diskon.

'''Test Case Self-Super Cashier'''
def create_transaction():
    transaction = Transaction()
#fungsi ini digunakan untuk menginisiasi transaksi pengguna ke dalam fungsi Transaction yang telah dibuat
    
    while True:
        print("\nMenu:")
        print("1. Add Item")
        print("2. Edit Item")
        print("3. Delete Item")
        print("4. Reset Transaction")
        print("5. Checkout")
        choice = input("Enter your choice (1-5): ")
#while True digunakan untuk membuat loop yang berulang dalam transaksi
        
        if choice == '1':
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter item quantity: "))
            item_price = float(input("Enter item price: "))
            transaction.add_item(item_name, item_quantity, item_price)
        elif choice == '2':
            item_index = int(input("Enter item index to edit: ")) - 1
            item_name = input("Enter new item name: ")
            item_price = float(input("Enter new item price: "))
            transaction.edit_item(item_index, item_name, item_price)
        elif choice == '3':
            item_index = int(input("Enter item index to delete: ")) - 1
            transaction.delete_item(item_index)
        elif choice == '4':
            transaction.reset_transaction()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")
#opsi-opsi pada fungsi if-elif yang telah dibuat memberikan opsi-opsi yang menjadi pilihan pelanggan
            
    transaction.display_transaction()
#fungsi ini digunakan untuk menampilkan rincian akhir transaksi yang telah dilakukan oleh pelanggan


# In[ ]:


create_transaction()

