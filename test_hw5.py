'''Test hw5.py
'''
import pytest
import datetime
import pandas as pd
from hw5 import car_at_light, safe_subtract, retrieve_age_eafp, retrieve_age_lbyl, \
    read_data, count_simba, get_day_month_year, compute_distance, sum_general_int_list


def test_car_at_light_red():
    light = 'red'
    exp_out = 'stop'
    out = car_at_light(light)

    assert out == exp_out

def test_car_at_light_green():
    light = 'green'
    exp_out = 'go'
    out = car_at_light(light)

    assert out == exp_out

def test_car_at_light_yellow():
    light = 'yellow'
    exp_out = 'wait'
    out = car_at_light(light)

    assert out == exp_out


def test_car_at_light_exception():
    light = 10

    with pytest.raises(Exception):
        out = car_at_light(light)

def test_safe_subtract_res():
    first_val = 10
    second_val = 5
    exp_out = 5
    out = safe_subtract(first_val, second_val)

    assert out == exp_out

def test_safe_subtract_type_error():
    first_val = '10'
    second_val = 5
    exp_out = None
    out = safe_subtract(first_val, second_val)

    assert out == exp_out

def test_safe_subtract_type_exception():
    first_val = 10
    second_val = 5

    with pytest.raises(Exception):
        out = safe_subtract(first_val, second_val, 10)

def test_retrieve_age_eafp_res():
    person = {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
    exp_out = 1987
    out = retrieve_age_eafp(person)

    assert out == exp_out

def test_retrieve_age_eafp_keyerror():
    person = {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
    exp_out = None
    out = retrieve_age_eafp(person)

    assert out == exp_out


def test_retrieve_age_lbyl_res():
    person = {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
    exp_out = 1987
    out = retrieve_age_lbyl(person)

    assert out == exp_out

def test_retrieve_age_lbyl_keyerror():
    person = {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
    exp_out = None
    out = retrieve_age_lbyl(person)

    assert out == exp_out

def test_read_data_nofile():
    exp_out = None
    out = read_data()

    assert out == exp_out  # no file data.csv hence just checking for that condition

def test_count_simba_res():
    l_strings = ["Simba and Nala are lions.", "I laugh in the face of danger.",
 "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
    exp_out = 3
    out = count_simba(l_strings)

    assert out == exp_out

def test_get_day_month_year():
    l_datetimes = [datetime.date.today(), datetime.date.today() - datetime.timedelta(days=1)]
    exp_out = pd.DataFrame({'day': [datetime.date.today().day, (datetime.date.today() - datetime.timedelta(days=1)).day], 'month': [datetime.date.today().month, (datetime.date.today() - datetime.timedelta(days=1)).month], 'year': [datetime.date.today().year, (datetime.date.today() - datetime.timedelta(days=1)).year]})
    out = get_day_month_year(l_datetimes)

    assert out.equals(exp_out)

def test_compute_distance():
    l_t_long_lat = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
    exp_out = [31.13186522205169, 157.00582786889402]
    out = compute_distance(l_t_long_lat)

    assert out == exp_out

def test_sum_general_int_list():
    int_l = [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]
    exp_out = 48
    out = sum_general_int_list(int_l)

    assert out == exp_out