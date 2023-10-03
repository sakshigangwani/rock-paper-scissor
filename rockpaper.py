import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x500")

        self.contacts = {}

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.pack()

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.pack()

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact, width=20, height=2)
        self.add_button.pack()

        self.contact_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.contact_listbox.pack()

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts, width=20, height=2)
        self.view_button.pack()

        self.search_label = tk.Label(root, text="Search:")
        self.search_label.pack()
        self.search_entry = tk.Entry(root, width=30)
        self.search_entry.pack()

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact, width=20, height=2)
        self.search_button.pack()

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact, width=20, height=2)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact, width=20, height=2)
        self.delete_button.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            self.contacts[name] = phone
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_entries()
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Name and phone fields are required.")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for name, phone in self.contacts.items():
            self.contact_listbox.insert(tk.END, f"{name}: {phone}")

    def search_contact(self):
        name = self.search_entry.get()
        if name in self.contacts:
            phone = self.contacts[name]
            messagebox.showinfo("Contact Found", f"{name}: {phone}")
        else:
            messagebox.showerror("Contact Not Found", f"Contact '{name}' not found.")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            selected_contact = self.contact_listbox.get(selected_index[0])
            selected_name, _ = selected_contact.split(":")
            new_phone = self.phone_entry.get()
            if selected_name in self.contacts:
                self.contacts[selected_name] = new_phone
                messagebox.showinfo("Success", "Contact updated successfully.")
                self.clear_entries()
                self.view_contacts()
            else:
                messagebox.showerror("Error", f"Contact '{selected_name}' not found.")
        else:
            messagebox.showerror("Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            selected_contact = self.contact_listbox.get(selected_index[0])
            selected_name, _ = selected_contact.split(":")
            if selected_name in self.contacts:
                del self.contacts[selected_name]
                messagebox.showinfo("Success", "Contact deleted successfully.")
                self.clear_entries()
                self.view_contacts()
            else:
                messagebox.showerror("Error", f"Contact '{selected_name}' not found.")
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
