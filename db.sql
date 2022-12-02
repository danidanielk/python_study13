create table search_location(
sl_no number(3) primary key,
sl_place_name varchar2(30char) not null,
sl_phone varchar2(20char) not null,
sl_x number(9,6)not null,
sl_y number(8,6) not null
);

select * from search_location
create sequence search_location_seq;
--NVL 함수 : 값이 null 일때 지정한 값으로 대치하는 함수.
--NVL(값,(값이)null일때 대체값)
select nvl(null,'-'),nvl('null','-')from dual;