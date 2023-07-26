# 라이브러리 설정----
library(dplyr)
library(data.table)
library(lubridate)
library(stringr)
library(clipr)

# 경로 설정----
setwd("/Users/sihoon/Desktop/FastCampus/Section_3/CH05")

# 데이터 불러오기----
ord_info <- fread("practice/List of Orders.csv") %>% tibble()
ord_prd <- fread("practice/Order Details.csv") %>% tibble()
cust_info <- fread("practice/Customer Segmentation.csv") %>% tibble()





# 데이터
ord_prd %>% 
  select(ord_cd, catg_1, ord_amt)

# 그룹핑
ord_prd %>% 
  select(ord_cd, catg_1, ord_amt) %>% 
  group_by(ord_cd)

ord_prd %>% 
  filter(ord_cd %in% c('B-25601', 'B-25602')) %>% 
  select(ord_cd, catg_1, ord_amt) %>% 
  group_by(ord_cd) %>% 
  summarise(sum_amt = sum(ord_amt), 
            n_prd = n(), 
            avg_amt = mean(ord_amt))

ord_prd %>% 
  group_by('catg_1', 'catg_2') %>% 
  summarise(sum_amt = sum(ord_amt), 
            n_prd = n(), 
            avg_amt = mean(ord_amt))

cust_info %>% 
  group_by(gender) %>%
  summarise(cust_n = n())

cust_info %>%
  group_by(job) %>% 
  summarise(cust_n = n()) %>%
  arrange(cust_n %>% desc)

cust_info %>%
  group_by(gender, job) %>% 
  summarise(cust_n = n()) %>% 
  arrange(gender, job, cust_n %>% desc)

cust_info %>% 
  group_by(gender, married) %>% 
  summarise(cust_n = n(),
            avg_age = mean(age)) %>% 
  arrange(gender, married %>% desc, cust_n %>% desc)

cust_info %>% 
  group_by(job) %>% 
  summarise(cust_n = n(), avg_age = mean(age), max_age = max(age), min_age = min(age)) %>% 
  arrange(cust_n %>% desc)

ord_prd %>% 
  left_join(ord_info) %>% 
  group_by(catg_1, state) %>% 
  summarise(rev = sum(ord_amt)) %>% 
  data.table() %>% # dcast를 사용하기위해 사용
  dcast.data.table(state ~ catg_1, value.var = "rev", sum) %>% 
  tibble()

ord_prd %>% 
  left_join(ord_info) %>% 
  mutate(ord_ymd = ord_dt %>% dmy) %>% 
  group_by(catg_1, ord_ymd) %>% 
  summarise(rev = sum(ord_amt)) %>% 
  data.table() %>% 
  dcast.data.table(ord_ymd ~ catg_1, value.var = "rev", fill = "na") %>% 
  tibble()

cust_info %>% 
  group_by(gender, married, graduated, spend) %>% 
  summarise(n = n()) %>% 
  dcast.data.table(gender + married + graduated ~ spend, value.var = "n", sum) %>% 
  select(gender, married, graduated, High, Average, Low)

cust_info %>% 
  left_join(ord_info) %>% 
  left_join(ord_prd) %>% 
  select(job, catg_1, ord_amt) %>% 
  group_by(job) %>% 
  summarise(avg_sales = mean(ord_amt))
  filter(job %>% nchar() > 1) %>% 
  arrange(avg_sales %>% desc)
  