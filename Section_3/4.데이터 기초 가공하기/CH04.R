library(dplyr)
library(data.table)
library(lubridate)
library(stringr)
library(clipr)

setwd("/Users/sihoon/Desktop/FastCampus/Section_3/CH04")

ord_info <- fread("practice/List of Orders.csv") %>% tibble()
ord_prd <- fread("practice/Order Details.csv") %>% tibble()
cust_info <- fread("practice/Customer Segmentation.csv") %>% tibble()
ord_info %>%  
  select(state, cust_nm)
ord_prd %>%
  select(ord_cd, ord_amt)
ord_prd %>%
  select(catg_1, qty)
catg_info <- ord_prd %>%
  select(catg_1, catg_2)

catg_info %>%
  head(10) %>%
  distinct(catg_1)

ord_info %>%
  filter(cust_nm == 'Pearl')

ord_info %>%  
  filter(cust_nm == 'Pearl', 
         city == "Pune")

ord_info <- ord_info %>%
  mutate(cust_nm = ifelse(nchar(cust_nm)<1, NA, cust_nm))

ord_info %>%
  filter(cust_nm %>% is.na)

ord_info %>%
  filter(state %>% str_detect ("adh"))

ord_prd %>%
  filter(ord_amt > 5000)

ord_info %>%
  filter(cust_nm == "Pooja", state == "Goa")

ord_prd %>%
  filter(catg_1 == "Clothing")

ord_prd %>%
  filter(catg_1 == "Clothing", 
         catg_2 == "T-shirt", 
         qty >= 10)

ord_prd %>%
  filter(ord_amt >= 1000, 
         ord_profit < 0)

ord_prt %>%
  filter(ord_amt >= 1000, 
         ord_profit < 0, 
         catg_1 %in% c("Clothing", "Electronics"))

ord_prd %>%  
  filter(ord_amt >= 1000,
         ord_profit < 0,
         catg_1 %in% c("Clothing", "Electronics"))


ord_prd %>%
  filter(catg_1 %>% str_detect("p"), 
         ord_profit == 0, 
         qty <= 2)

gender_info <- cust_info %>%
  cust_info %>%
    mutate(gender_simple = gender %>% str_sub(1, 1)) %>%
    select(cust_nm, gender_simple)

cust_info %>%
  filter(!tenure %>% is.na) %>%
  mutate(t_gro = ifelse(tenure == 1, "신입", "경력"), gender_simple = gender %>% str_sub(1, 1)) %>% 
  select(cust_nm, gender_simple, t_gro)

gender_info <- cust_info %>%
  mutate(gender_simple = gender %>% str_sub(1, 1)) %>%
  select(cust_nm, gender_simple)


tenure_info <- cust_info %>%
  filter(!tenure %>% is.na) %>%
  mutate(t_gro = ifelse(tenure <= 1, '신입', '경력'),
         gender_simple = gender %>% str_sub(1, 1)) %>%
  select(cust_nm, gender_simple, t_gro)
tenure_info

cust_info %>%
  mutate(t_gro = ifelse(tenure == 1, '신입', '경력'), 
         gender_simple = gender %>% str_sub(1, 1), 
         f_gro = ifelse(family == 1, '1인가구',
                        ifelse(family == 2, '2인가구', '대가구'))) %>%
  select(cust_nm, gender_simple, t_gro, f_gro)
ord_info
addr_info <- ord_info %>%
  mutate(addr = paste(state, city)) %>%
  select(cust_nm, addr)
ord_info

addr_info
catg_1
ord_prd

price_200_info <- ord_prd %>%
  mutate(price = ord_amt/qty) %>%
  filter(price >= 200)
price_200_info

cust_info %>%
  arrange(age)
cust_info %>%
  select(cust_nm, age, tenure, job) %>%
  arrange(age %>% desc, tenure %>% desc)

ord_prd %>%
  mutate(ord_dis = ord_amt-ord_profit) %>% 
  arrange(ord_dis %>% desc) %>%
  select(ord_cd, ord_amt, ord_profit, ord_dis)

week_sales <- left_join(ord_info, ord_prd) %>%
  select(ord_dt, ord_cd, ord_amt) %>%
  mutate(ord_week = ord_dt %>% dmy %>% week, 
         ord_dow = ord_dt %>% dmy %>% wday(label = T)) %>%
  select(ord_week, ord_dow, ord_amt)
week_sales
