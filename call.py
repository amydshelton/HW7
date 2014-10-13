"""
call.py - Telemarketing script that displays the next name 
          and phone number of a Customer to call.

          This script is used to drive promotions for 
          specific customers based on their order history.
          We only want to call customers that have placed
          an order of over 20 Watermelons.

"""

# Load the customers from the passed filename
# Return a dictionary containing the customer data
#    (key = customer_id)
def load_customers(filename):
    customers = {}
    f = open(filename)

    # First line of the file should be the header, 
    #   split that into a list
    header = f.readline().rstrip().split(',')

    # Process each line in a file, create a new
    #   dict for each customer
    for line in f:
        data = line.rstrip().split(',')
        called = data[5]

        # only add customers to the dictionary who haven't been called yet
        if called == '':
            customer = {}

            # Loop through each column, adding the data
            #   to the dictionary using the header keys
            for i in range(len(header)):
                customer[header[i]] = data[i]

            # Add the customer to our dictionary by customer id
            customers[customer['customer_id']] = customer

    # Close the file
    f.close()

    #returns a dictionary, where cust ID is the key and all other cust info (name, customer Id,
        # phone number, when they were called, email address) is the value
    return customers

#print load_customers('reduced_customers.csv')



# Load the orders from the passed filename
# Return a list of all the orders
def load_orders(filename):
    orders = []
    f = open(filename)

    # First line of the file should be the header, 
    #   split that into a list
    header = f.readline().rstrip().split(',')

    # Process each line in a file, create a new
    #   dict for each order
    for line in f:
        data = line.rstrip().split(',')
        num_watermelons = int(data[9])

        #only add the orders with over 20 watermelons
        if num_watermelons > 20:
            # Create a dictionary for the order by combining
            #   the header list and the data list
            order = dict(zip(header, data))

            # Add the order to our list of orders to return
            orders.append(order)

    # Close the file
    f.close()

    #returns a list of dictionaries. one dictionary per row of the file.

    return orders

#print "Orders.csv printout = ", load_orders("reduced_orders.csv")

def display_customer(customer):
    print "---------------------"
    print "Next Customer to call"
    print "---------------------\n"
    print "Name: ", customer.get('first', ''), customer.get('last', '')
    print "Phone: ", customer.get('telephone', '')
    print "\n"


def update_call_log(old_filename, new_filename, customer):
    call_status = raw_input("Call achieved? Y or N > ")
    customer_id = customer.get('customer_id', 0)
    first = customer.get('first', 0)
    last = customer.get('last', 0)
    email = customer.get('email', 0)
    telephone = customer.get('telephone', 0)
    called = "today's date"
    reconstructed_data = customer_id + "," + first + ',' + last + ',' + email + ',' + telephone + ','

    if call_status == "Y" or call_status ==  "y":
        reconstructed_call_achieved = reconstructed_data + called + ',\n'
        with open(new_filename,"a") as newfile:
                    newfile.write(reconstructed_call_achieved)
    else:
        reconstructed_call_not_achieved = reconstructed_data + ',,\n'



def main():

  #  set up new file
  #  old = open('reduced_customers.csv')
  #  new = open('newfile.csv')

   # header = old.readline().rstrip().split(',')
   # header_string = ",".join(header) + "\n"
   # with open('newfile.csv', "a") as newfile:
   #     newfile.write(header_string)

    #new.close()

    # Load data from our csv files

    customers = load_customers('customers.csv')
    orders    = load_orders('orders.csv')

    # Loop through each order
    for order in orders:
        customer = customers.get(order.get('customer_id', 0), 0)
        if customer == 0:
            print "No more customers to call! Go have a drink!"
            continue
        else:
            display_customer(customer)
          #  update_call_log(old, 'newfile.csv', customer)
            break

if __name__ == '__main__':
    main()