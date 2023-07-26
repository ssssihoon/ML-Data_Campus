source("/Users/sihoon/Desktop/source/source.R")
setwd("/Users/sihoon/Desktop/FastCampus/Section_3/CH08")

library(echarts4r)

cust_info <- fread("/Users/sihoon/Desktop/FastCampus/Section_3/CH08/practice/Customer Segmentation.csv")
ord_info <- fread("/Users/sihoon/Desktop/FastCampus/Section_3/CH08/practice/List of Orders.csv")
ord_prd <- fread("/Users/sihoon/Desktop/FastCampus/Section_3/CH08/practice/Order Details.csv")


# 월별 매출액 현황은 어떠한가?
line_df <- ord_info %>% 
  left_join(ord_prd) %>% 
  mutate(ord_month = ord_dt %>% dmy %>% str_sub(1, 7)) %>% 
  group_by(ord_month) %>% 
  summarise(revenue = sum(ord_amt))
line_df

line_df %>% 
  e_charts(ord_month) %>% 
  e_line(revenue, name = "매출액", smooth = TRUE)
  
ord_info %>% 
  left_join(ord_prd) %>% 
  mutate(ord_q = ord_dt %>% dmy %>% quarter(with_year = T) %>% as.character()) %>% 
  group_by(ord_q) %>% 
  summarise(revenue = sum(ord_amt), 
            profit = sum(ord_profit)) %>% 
  e_charts(ord_q) %>% 
  e_line(revenue) %>% 
  e_line(profit) %>% 
  e_theme("dark-fresh-cut") %>% 
  e_color(c("blue", "red")) %>% 
  e_toolbox_feature(feature = c("dataZoom", "dataView", "saveAsImage")) %>% # 데이터를 줌, 뷰, 다운로드 가능하게 함
  e_tooltip(trigger = "axis") %>%  # 데이터에 커서를 가져다 놓으면 값이 무엇인지 알려주는 기능
  e_datazoom(x_index = 0, type = "slider") %>% # x축에 스크롤이 가능하게
  e_datazoom(y_index = 0, type = "slider") # x축에 스크롤이 가능하게

ord_info %>% 
  left_join(cust_info) %>% 
  left_join(ord_prd) %>% 
  mutate(ord_month = ord_dt %>% dmy %>% as.character() %>% str_sub(1, 7), 
         ord_year = ord_dt %>% dmy %>% as.character() %>% substr(1, 4)) %>% 
  filter(ord_year == "2018") %>% 
  group_by(ord_month, gender) %>% 
  summarise(order = n_distinct(ord_cd)) %>% 
  group_by(gender) %>% 
  e_chart(ord_month) %>% 
  e_bar(order) %>% 
  e_color(c("red", "blue"))
           

ord_prd %>% 
  left_join(ord_info) %>% 
  left_join(cust_info) %>% 
  mutate(ord_dt = ord_dt %>% dmy() %>% ymd(), 
         month = ord_dt %>% substr(1, 7)) %>% 
  group_by(month) %>% 
  summarise(Revenue = sum(ord_amt), 
            Profit = sum(ord_profit)) %>% 
  e_charts(month) %>% 
  e_bar(Profit, barWidth = 10) %>% 
  e_pictorial(Revenue, 
              symbol = "Circle", 
              symbolRepeat = TRUE, 
              symbolSize = c(10, 10)) # 바의 칸 구분 
  
ord_info %>% 
  left_join(ord_prd) %>% 
  left_join(cust_info) %>% 
  mutate(ord_month = ord_dt %>% dmy %>% str_sub(1, 7)) %>% 
  select(ord_month, ord_amt, ord_cd) %>% 
  group_by(ord_month, ord_cd) %>% 
  summarise(revenue = sum(ord_amt),
            order = n()) %>% 
  group_by(ord_month) %>% 
  summarise(revenue = sum(revenue), 
            order = n()) %>% 
  e_chart(ord_month) %>% 
  e_line(revenue, color = "Red", y_index = 1) %>% 
  e_bar(order, y_index = 0)
