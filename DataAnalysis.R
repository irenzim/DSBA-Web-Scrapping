mean_value <- mean(books$Disc)
median_value<-median(books$Disc)

# Load the tidyverse package
library(tidyverse)

# Calculate the average discount for each year
Disc<-books$Discount
avg_discount <- books %>%
  group_by(Year) %>%
  summarise(mean_discount = mean(Disc, na.rm = TRUE))

# Print the average discount for each year
print(avg_discount)

#ploting the results
Year<-(books$Year)

ggplot(data = avg_discount, aes(x = Year, y = avg_discount)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(x = "Year", y = "Average Discount") +
  ggtitle("Average Discount by Year") +
  theme_minimal() +
  
  # Print the table
  print(table_data)

#calculate the average discount by cover type
Covertype<-(books$Cover_type)
avg_discount_cover <- books %>%
  group_by(Cover_type) %>%
  summarise(mean_disc_cover = mean(Disc, na.rm = TRUE))
print(avg_discount_cover)


#ploting the results
ggplot(data = avg_discount_cover, aes(x = Year, y = mean_disc_cover)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(x = "CoverType", y = "Average Discount") +
  ggtitle("Average Discount by Cover type") +
  theme_minimal()


#To make the histograms of price and discount

Price<-book$Price
ggplot(data = book, aes(x = Price)) +
  geom_histogram(binwidth = 10, fill = "steelblue", color = "white") +
  labs(x = "Price", y = "Frequency") +
  ggtitle("Histogram of Prices") +
  theme_minimal() 

Disc<-book$Disc
ggplot(data = book, aes(x = Disc)) +
  geom_histogram(binwidth = 1, fill = "steelblue", color = "white") +
  labs(x = "Discount", y = "Frequency") +
  ggtitle("Histogram of Discounts") +
  theme_minimal() 

#To make a scatter graph of price and discount. 
ggplot(data = book, aes(x = Price, y = Disc)) +
  geom_point(color = "steelblue") +
  labs(x = "Price", y = "Discount") +
  ggtitle("Correlation between Price and Discount") +
  theme_minimal()

#Calculating the correlation of price and discount
correlation <- cor(book$Disc, book$Price)
print(correlation)