import os
import pickle
import re




if __name__ == '__main__':
    root_path = '/Users/rampage/PycharmProjects/Simulators/ENACT/action_sequence/'

    # for name in os.listdir(root_path):
    #     file_path = os.path.join(root_path, name)
    #     action_list_file_path = os.path.join(file_path, 'action_sequence.pkl')
    #
    #     with open(action_list_file_path, 'rb') as file:
    #         # Use pickle.load() to read the list from the file
    #         loaded_list = pickle.load(file)
    #     parts = re.split(r'(?=\d)', name, maxsplit=1)
    #     task_name = parts[0].replace('_', ' ').rstrip()
    #     print(task_name)
    #     print("================================================================================================================")
    #     print(loaded_list)
    #     print("================================================================================================================")


    # file_name = ""
    # with open(os.path.join(os.path.join(root_path, file_name),'action_sequence.pkl'), 'wb') as f:
    #     pickle.dump(corrected_action_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    # print(f"file {file_name} has been corrected")



    # canning food
    correct_list =['navigate_to(cutting_board_208)_1',
                   'grasp(carving_knife_207)_1',
                   'navigate_to(countertop_kelzer_0)_1',
                   'grasp(cutting_board_208)_1',
                   'navigate_to(drop_in_sink_awvzkn_0)_1',
                   'place_ontop(cutting_board_208, drop_in_sink_awvzkn_0)_1',
                   'navigate_to(countertop_kelzer_0)_2',
                   'place_ontop(carving_knife_207, countertop_kelzer_0)_1',
                   'navigate_to(fridge_dszchb_0)_1', 'open(fridge_dszchb_0)_1',
                   'grasp(steak_212)_1', 'grasp(pineapple_211)_1',
                   'close(fridge_dszchb_0)_1',
                   'navigate_to(countertop_kelzer_0)_3',
                   'place_ontop(steak_212, cutting_board_208)_1',
                   'place_ontop(pineapple_211, cutting_board_208)_1'
                   'grasp(carving_knife_207)_2',
                   'slice-carvingknife(steak_212, carving_knife_207, countertop_kelzer_0)_1',
                   'place_ontop(carving_knife_207, countertop_kelzer_0)_2',
                   'navigate_to(bottom_cabinet_fancyy_0)_1',
                   'open(bottom_cabinet_fancyy_0)_1',
                   'grasp(bowl_209)_1',
                   'grasp(bowl_210)_1',
                   'navigate_to(countertop_kelzer_0)_4',
                   'place_ontop(bowl_209, countertop_kelzer_0)_1',
                   'place_ontop(bowl_210, countertop_kelzer_0)_1',
                   'grasp(cutting_board_208)_2',
                   'place_inside(steak_212,bowl_209)_1',
                   'place_ontop(cutting_board_208, drop_in_sink_awvzkn_0)_2',
                   'grasp(bowl_209)_2',
                   'navigate_to(bottom_cabinet_fancyy_0)_2',
                   'open(bottom_cabinet_fancyy_0)_2',
                   'place_inside(bowl_209, bottom_cabinet_fancyy_0)_1',
                   'navigate_to(countertop_kelzer_0)_5',
                   'slice-carvingknife(pineapple_211, carving_knife_207, countertop_kelzer_0)_1',
                   'place_ontop(carving_knife_207, countertop_kelzer_0)_3',
                   'grasp(cutting_board_208)_3',
                   'place_inside(pineapple_211,bowl_210)_1',
                   'place_ontop(cutting_board_208, drop_in_sink_awvzkn_0)_3',
                   'grasp(bowl_210)_2',
                   'navigate_to(bottom_cabinet_fancyy_0)_3',
                   'place_inside(bowl_210, bottom_cabinet_fancyy_0)_1']

    file_name = "canning_food_1751278778230696"
    with open(os.path.join(os.path.join(root_path, file_name),'action_sequence.pkl'), 'wb') as f:
        pickle.dump(correct_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"file {file_name} has been corrected")

    # getting organized for work
    correct_list = ['navigate_to(desk_uqcmzf_0)_1',
                    'grasp(monitor_86)',
                    'place_ontop(desk_uqcmzf_0, monitor_86)_1',
                    'grasp(keyboard_91)_1', 'place_nextto(keyboard_91, monitor_86)_1',
                    'grasp(mouse_92)_1', 'place_nextto(mouse_92, desk_uqcmzf_0)_1'
                    'navigate_to(swivel_chair_iiihwn_0)_1',
                    'grasp(pen_89)_1',
                    'navigate_to(desk_uqcmzf_0)_2',
                    'place_ontop(pen_89, desk_uqcmzf_0)_1',
                    'navigate_to(swivel_chair_iiihwn_0)_2'
                    'grasp(folder_88)_1', 'navigate_to(desk_uqcmzf_0)_3', 'place_ontop(folder_88, desk_uqcmzf_0)_1'
                    'grasp(notebook_90)_1', 'place_ontop(notebook_90, folder_88)_1', 'grasp(pen_89)_2', 'place_ontop(pen_89, notebook_90)_1']

    file_name = "getting_organized_for_work_1749534060191222"
    with open(os.path.join(os.path.join(root_path, file_name), 'action_sequence.pkl'), 'wb') as f:
        pickle.dump(correct_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"file {file_name} has been corrected")

    # making pizza
    correct_list = ['navigate_to(bar_egwapq_0)_1', 'grasp(carving_knife_77)_1', 'navigate_to(chopping_board_78)_1', 'slice-carvingknife(vidalia_onion_80,carving_knife_77,chopping_board_78)_1', 'slice-carvingknife(mushroom_81,carving_knife_77,chopping_board_78)_1',
                    'place_ontop(carving_knife_77,bar_egwapq_0)_1',
                    'navigate_to(fridge_petcxr_0)_1',
                    'open(fridge_petcxr_0)_1',
                    'grasp(tupperware_75)_1',
                    'navigate_to(bar_egwapq_0)_2',
                    'place_ontop(tupperware_75,bar_egwapq_0)_1',
                    'open(fridge_petcxr_0)_2',
                    'close(fridge_petcxr_0)_1',
                    'navigate_to(baking_sheet_79)_1',
                    'grasp(half_mushroom_81_0)_1',
                    'place_ontop(half_mushroom_81_0,pizza_dough_87)_1',
                    'grasp(pepperoni_83)_1',
                    'place_ontop(pepperoni_83,pizza_dough_87)_1',
                    'grasp(tupperware_75)_2',
                    'place_ontop(grated_cheese,pizza_dough_87)_1',
                    'place_ontop(tupperware_75,bar_egwapq_0)_2',
                    'navigate_to(oven_ffitak_0)_1',
                    'open(oven_ffitak_0)_1',
                    'navigate_to(baking_sheet_79)_2',
                    'grasp(baking_sheet_79)_1',
                    'navigate_to(oven_ffitak_0)_2',
                    'place_inside(baking_sheet_79,oven_ffitak_0)_1',
                    'close(oven_ffitak_0)_1'
                    'toggle_on(oven_ffitak_0)_1']

    file_name ='make_pizza_1754278662570814'
    with open(os.path.join(os.path.join(root_path, file_name), 'action_sequence.pkl'), 'wb') as f:
        pickle.dump(correct_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"file {file_name} has been corrected")

    # cleaning up plates and food
    correct_list= ['navigate_to(fridge_petcxr_0)_1', 'open(fridge_petcxr_0)_1', 'navigate_to(breakfast_table_xftrki_0)_1',
     'grasp(plate_93)_1', 'navigate_to(fridge_petcxr_0)_2', 'place_inside(plate_93, fridge_petcxr_0)_1',
     'navigate_to(breakfast_table_xftrki_0)_2', 'grasp(plate_94)_1', 'navigate_to(fridge_petcxr_0)_3',
     'place_inside(plate_94, fridge_petcxr_0)_1', 'close(fridge_petcxr_0)_1','navigate_to(breakfast_table_xftrki_0)_3', 'grasp(bowl_92)_1',
     'grasp(bowl_91)_1', 'navigate_to(drop_in_sink_lkklqs_0)_1', 'place_inside(bowl_91, drop_in_sink_lkklqs_0)_1',
     'place_inside(bowl_92, drop_in_sink_lkklqs_0)_1']

    file_name = "cleaning_up_plates_and_food_1747631958405370"
    with open(os.path.join(os.path.join(root_path, file_name), 'action_sequence.pkl'), 'wb') as f:
        pickle.dump(correct_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"file {file_name} has been corrected")

    # cook cabbage
    correct_list = ['navigate_to(fridge_dszchb_0)_1', 'open(fridge_dszchb_0)_1', 'grasp(head_cabbage_212)_1',
                    'grasp(chili_211)_1',
                    'close(fridge_dszchb_0)_1',
                    'navigate_to(countertop_kelker_0)_1',
                    'place_ontop(chili_211,plate_207)_1'
                    'place_ontop(head_cabbage_212, cutting_board_210)_1',
                    'grasp(frying_pan_208)_1',
                    'place_ontop(frying_pan_208,burner_mjvqii_0)_1',
                    'grasp(carving_knife_209)_1',
                    'slice-carvingknife(head_cabbage_212, carving_knife_209)_1',
                    'place_ontop(carving_knife_209,countertop_kelker_0)_1',
                    'grasp(cutting_board_210)_1',
                    'place_inside(head_cabbage_212,frying_pan_208)_1',
                    'place_ontop(cutting_board_210,countertop_kelker_0)_1'
                    'grasp(chili_211)_2',
                    'place_ontop(chili_211,cutting_board_210)',
                    'grasp(carving_knife_209)_2',
                    'slice-carvingknife(chili_211, carving_knife_209)_1',
                    'place_ontop(carving_knife_209,countertop_kelker_0)_2',
                    'grasp(cutting_board_210)_2',
                    'place_inside(chili_211,frying_pan_208)_1',
                    'place_ontop(cutting_board_210,countertop_kelker_0)_2',
                    'toggle_on(frying_pan_208)_1']

    file_name = "cook_cabbage_1753781960466556"
    with open(os.path.join(os.path.join(root_path, file_name), 'action_sequence.pkl'), 'wb') as f:
        pickle.dump(correct_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"file {file_name} has been corrected")


    # preparing lunch box
    correct_list = ['navigate_to(countertop_kelker_0)_1',
                    'grasp(packing_box_210)_1',
                    'place_ontop(packing_box_210,burner_mjvqii_0)_1',
                    'navigate_to(chopping_board_211)_1', 'grasp(half_apple_213)_1', 'place_inside(half_apple_213,packing_box_210)_1', 'grasp(club_sandwich_209)_1', 'place_inside(club_sandwich_209,packing_box_210)_1', 'grasp(half_apple_212)_1', 'place_inside(half_apple_212,packing_box_210)_1', 'grasp(chocolate_chip_cookie_207)_1', 'place_inside(chocolate_chip_cookie_207,packing_box_210)_1', 'navigate_to(fridge_dszchb_0)_1', 'open(fridge_dszchb_0)_1', 'grasp(bottle_of_tea_208)_1',
                    'close(fridge_dszchb_0)_1',
                    'navigate_to(countertop_kelker_0)_2', 'place_inside(bottle_of_tea_208,packing_box_210)_1']

    file_name = "preparing_lunch_box_1748410854863188"
    with open(os.path.join(os.path.join(root_path, file_name), 'action_sequence.pkl'), 'wb') as f:
        pickle.dump(correct_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"file {file_name} has been corrected")


    # clean up your desk
    correct_list = ['navigate_to(eames_chair_hndxiw_0)_1',
                    'grasp(folder_231)_1',
                    'navigate_to(bookcase_jaysra_0)_1',
                    'place_inside(folder_231,bookcase_jaysra_0)_1',
                    'navigate_to(eames_chair_hndxiw_0)_2',
                    'grasp(eames_chair_hndxiw_0)_1',
                    'place_under(eames_chair_hndxiw_0,desk_bhkhxo_0)_1',
                    'navigate_to(desk_bhkhxo_0)_1',
                    'grasp(pencil_case_224)_1',
                    'grasp(pen_228)_1', 'place_inside(pen_228,pencil_case_224)_1',
                    'grasp(pencil_230)_1',
                    'place_inside(pencil_230,pencil_case_224)_1',
                    'grasp(pen_229)_1',
                    'place_inside(pen_229,pencil_case_224)_1',
                    'place_ontop(pencil_case_224,desk_bhkhxo_0)_1',
                    'navigate_to(desk_bhkhxo_0)_2',
                    'grasp(paperback_book_226)_1',
                    'navigate_to(bookcase_jaysra_0)_2',
                    'place_inside(paperback_book_226,bookcase_jaysra_0)_1',
                    'navigate_to(desk_bhkhxo_0)_3',
                    'grasp(paperback_book_225)_1',
                    'navigate_to(bookcase_jaysra_0)_3',
                    'place_inside(paperback_book_225,bookcase_jaysra_0)_1',
                    'navigate_to(desk_bhkhxo_0)_4',
                    'grasp(folder_232)_1',
                    'navigate_to(bookcase_jaysra_0)_4',
                    'place_inside(folder_232,bookcase_jaysra_0)_1',
                    'navigate_to(bed_rrcvaq_1)_1',
                    'grasp(laptop_233)_1',
                    'navigate_to(desk_bhkhxo_0)_5',
                    'place_ontop(laptop_233,desk_bhkhxo_0)_1',
                    'navigate_to(bookcase_jaysra_0)_5',
                    'grasp(stapler_227)_1',
                    'navigate_to(desk_bhkhxo_0)_6',
                    'place_ontop(stapler_227,desk_bhkhxo_0)_1']

    file_name = "clean_up_your_desk_1754374141392130"
    with open(os.path.join(os.path.join(root_path, file_name), 'action_sequence.pkl'), 'wb') as f:
        pickle.dump(correct_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"file {file_name} has been corrected")


    # sorting household items
    correct_list = ['navigate_to(sliding_door_tprpvb_10)_1', 'open(sliding_door_tprpvb_10)_1', 'navigate_to(hamper_226)_1', 'grasp(bottle_of_detergent_228)_1', 'grasp(bottle_of_detergent_227)_1', 'navigate_to(multi_station_furniture_sink_upwldu_0)_1', 'place_under(bottle_of_detergent_227,multi_station_furniture_sink_upwldu_0)_1', 'place_under(bottle_of_detergent_228,multi_station_furniture_sink_upwldu_0)_1',
                    'navigate_to(hamper_226)_2',
                    'grasp(box_of_sanitary_napkins_224)_1',
                    'navigate_to(hamper_225)_1',
                    'grasp(soap_dispenser_223)_1', 'navigate_to(multi_station_furniture_sink_upwldu_0)_2',
                    'place_ontop(soap_dispenser_223,multi_station_furniture_sink_upwldu_0)_1', 'navigate_to(shelf_fjozhc_0)_1',
                    'place_ontop(box_of_sanitary_napkins_224,shelf_fjozhc_0)_1',
                    'navigate_to(hamper_225)_2', 'grasp(tube_of_toothpaste_222)_1', 'grasp(toothbrush_221)_1', 'navigate_to(coffee_cup_220)_1', 'place_inside(toothbrush_221,coffee_cup_220)_1', 'place_inside(tube_of_toothpaste_222,coffee_cup_220)_1']

    file_name = "sorting_household_items_1753681589078441"
    with open(os.path.join(os.path.join(root_path, file_name), 'action_sequence.pkl'), 'wb') as f:
        pickle.dump(correct_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"file {file_name} has been corrected")

    # storing food
    correct_list = ['navigate_to(bottom_cabinet_fancyy_0)_1',
                    'open(bottom_cabinet_fancyy_0)_1',
                    'navigate_to(countertop_kelzer_0)_1',
                    'grasp(box_of_oatmeal_213)_1',
                    'navigate_to(bottom_cabinet_fancyy_0)_2',
                    'place_inside(box_of_oatmeal_213, bottom_cabinet_fancyy_0)_1',
                    'navigate_to(countertop_kelzer_0)_2',
                    'grasp(bottle_of_olive_oil_209)_1','grasp(bottle_of_olive_oil_210)_1',
                    'navigate_to(bottom_cabinet_fancyy_0)_3',
                    'place_inside(bottle_of_olive_oil_210, bottom_cabinet_fancyy_0)_1',
                    'place_inside(bottle_of_olive_oil_209, bottom_cabinet_fancyy_0)_1',
                    'navigate_to(countertop_kelzer_0)_3',
                    'grasp(jar_of_sugar_207)_1',
                    'grasp(jar_of_sugar_208)_1',
                    'navigate_to(bottom_cabinet_fancyy_0)_4',
                    'place_inside(jar_of_sugar_208, bottom_cabinet_fancyy_0)_1',
                    'place_inside(jar_of_sugar_207, bottom_cabinet_fancyy_0)_1',
                    'navigate_to(countertop_kelzer_0)_4',
                    'grasp(bag_of_chips_211)_1',
                    'grasp(bag_of_chips_212)_1',
                    'navigate_to(bottom_cabinet_fancyy_0)_5',
                    'place_inside(bag_of_chips_211, bottom_cabinet_fancyy_0)_1',
                    'place_inside(bag_of_chips_212, bottom_cabinet_fancyy_0)_1',
                    'navigate_to(countertop_kelzer_0)_5',
                    'grasp(box_of_oatmeal_214)_1',
                    'navigate_to(bottom_cabinet_fancyy_0)_6',
                    'place_inside(box_of_oatmeal_214, bottom_cabinet_fancyy_0)_1']

    file_name = "storing_food_1754046824351550"
    with open(os.path.join(os.path.join(root_path, file_name), 'action_sequence.pkl'), 'wb') as f:
        pickle.dump(correct_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"file {file_name} has been corrected")


    # chop an onion
    correct_list = ['navigate_to(bar_egwapq_0)_1',
                    'grasp(cutting_board_76)_1',
                    'place_nextto(cutting_board_76,parer_74)_1',
                    'navigate_to(drop_in_sink_lkklqs_0)_1', 'grasp(vidalia_onion_75)_1', 'navigate_to(bar_egwapq_0)_2',
                    'place_ontop(vidalia_onion_75,cutting_board_76)_1',
                    'grasp(parer_74)_1',
                    'slice(vidalia_onion_75,parer_74)_1',
                    'place_ontop(parer_74,bar_egwapq_0)_1',
                    'grasp(cutting_board_76)_2', 'place_inside(vidalia_onion_75,bowl_73)_1',
                    'place_ontop(cutting_board_76,drop_in_sink_lkklqs_0)_1']

    file_name = "chop_an_onion_1753875198396811"
    with open(os.path.join(os.path.join(root_path, file_name), 'action_sequence.pkl'), 'wb') as f:
        pickle.dump(correct_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"file {file_name} has been corrected")


    # cook bacon
    correct_list = ['navigate_to(fridge_dszchb_0)_1', 'open(fridge_dszchb_0)_1', 'grasp(tray_208)_1', 'close(fridge_dszchb_0)_1',
                    'navigate_to(burner_mjvqii_0)_1',
        'place_ontop(tray_208,burner_mjvqii_0)_1', 'grasp(frying_pan_207)_1', 'place_ontop(frying_pan_207, burner_mjvqii_0)_1',
        'navigate_to(tray_208)_1',
        "grasp(tray_208)_2",
        "place_inside(bacon_211, frying_pan_207)_1",
        "place_inside(bacon_210, frying_pan_207)_1",
        "place_inside(bacon_213, frying_pan_207)_1",
        "place_inside(bacon_214, frying_pan_207)_1",
        "place_inside(bacon_209, frying_pan_207)_1",
        "place_inside(bacon_212, frying_pan_207)_1",
        "place_ontop(tray_208,burner_mjvqii_0)_2",
        "toggle_on(burner_mjvqii_0)_1"]

    file_name = "cook_bacon_1750238326537465"
    with open(os.path.join(os.path.join(root_path, file_name), 'action_sequence.pkl'), 'wb') as f:
        pickle.dump(correct_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"file {file_name} has been corrected")

    # slicing vegetables
    correct_list = ['navigate_to(fridge_dszchb_0)_1', 'open(fridge_dszchb_0)_1',
                    'grasp(bell_pepper_214)_1',
                    'grasp(bell_pepper_213)_1',
                    'navigate_to(countertop_kelzer_0)_1', 'place_ontop(bell_pepper_214, cutting_board_210)_1','place_ontop(bell_pepper_213, cutting_board_210)_1',
                    'navigate_to(fridge_dszchb_0)_2',
                    'grasp(beet_211)_1',
                    'grasp(beet_212)_1',
                    'navigate_to(countertop_kelzer_0)_2',
                    'place_ontop(beet_211, cutting_board_209)_1',
                    'place_ontop(beet_212, cutting_board_209)_1',
                    'navigate_to(fridge_dszchb_0)_3', 'grasp(zucchini_208)_1',
                    'close(fridge_dszchb_0)_1',
                    'navigate_to(countertop_kelzer_0)_3',
                    'place_ontop(zucchini_208, cutting_board_209)_1',
                    'grasp(parer_207)_1',
                    'slice(beet_212, parer_207, robot_r1)_1',
                    'slice(beet_211, parer_207, robot_r1)_1',
                    'slice(zucchini_208, parer_207, robot_r1)_1',
                    'slice(bell_pepper_214, parer_207, robot_r1)_1',
                    'slice(bell_pepper_213, parer_207, robot_r1)_1',
                    'place_ontop(parer_207, countertop_kelzer_0)_1']

    file_name = "slicing_vegetables_1754479015822159"
    with open(os.path.join(os.path.join(root_path, file_name), 'action_sequence.pkl'), 'wb') as f:
        pickle.dump(correct_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"file {file_name} has been corrected")

    # putting away Halloween decorations
    correct_list =['navigate_to(pillar_candle_89)_1',
                   'grasp(pillar_candle_89)_1',
                   'navigate_to(bottom_cabinet_rhdbzv_0)_1',
                   'open(bottom_cabinet_rhdbzv_0)_1',
                   'place_inside(pillar_candle_89, bottom_cabinet_rhdbzv_0)_1',
                   'navigate_to(pillar_candle_91)_1', 'grasp(pillar_candle_91)_1',
                   'navigate_to(pillar_candle_90)_1', 'grasp(pillar_candle_90)_1',
                   'navigate_to(bottom_cabinet_rhdbzv_0)_2',
                   'place_inside(pillar_candle_91, bottom_cabinet_rhdbzv_0)_1', 'place_inside(pillar_candle_90, bottom_cabinet_rhdbzv_0)_1',
                   'close(bottom_cabinet_rhdbzv_0)_1',
                   'navigate_to(pumpkin_93)_1', 'grasp(pumpkin_93)_1',
                   'navigate_to(bottom_cabinet_rhdbzv_0)_3'
                   'open(bottom_cabinet_rhdbzv_0)_2',
                   'place_inside(pumpkin_93, bottom_cabinet_rhdbzv_0)_1'
                   'navigate_to(pumpkin_94)_1', 'grasp(pumpkin_94)_1',
                   'navigate_to(bottom_cabinet_rhdbzv_0)_4', 'place_inside(pumpkin_94, bottom_cabinet_rhdbzv_0)_1',
                   'close(bottom_cabinet_rhdbzv_0)_2',
                   'navigate_to(cauldron_92)_1', 'grasp(cauldron_92)_1', 'navigate_to(breakfast_table_xftrki_0)_1', 'place_nextto(cauldron_92, breakfast_table_xftrki_0)_1']

    file_name = "putting_away_Halloween_decorations_1747389873610361"
    with open(os.path.join(os.path.join(root_path, file_name), 'action_sequence.pkl'), 'wb') as f:
        pickle.dump(correct_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"file {file_name} has been corrected")

    # can meat
    correct_list = ['navigate_to(top_cabinet_lkxmne_2)_1',
                    'open(top_cabinet_lkxmne_2)_1',
                    'grasp(hinged_jar_236)_1',
                    'navigate_to(bar_udatjt_0)_1', 'open(hinged_jar_236)_1', 'grasp(bratwurst_233)_1', 'place_inside(bratwurst_233, hinged_jar_236)_1', 'grasp(bratwurst_231)_1', 'place_inside(bratwurst_231, hinged_jar_236)_1',
                    'close(hinged_jar_236)_1',
                    'navigate_to(top_cabinet_lkxmne_2)_2', 'place_inside(hinged_jar_236, top_cabinet_lkxmne_2)_1',
                    'grasp(hinged_jar_235)_1', 'navigate_to(bar_udatjt_0)_2',
                    'open(hinged_jar_235)_1', 'grasp(bratwurst_230)_1', 'place_inside(bratwurst_230, hinged_jar_235)_1', 'grasp(bratwurst_232)_1', 'place_inside(bratwurst_232, hinged_jar_235)_1', 'grasp(hinged_jar_235)_2',
                    'close(hinged_jar_235)_1',
                    'navigate_to(top_cabinet_lkxmne_2)_3', 'place_inside(hinged_jar_235, top_cabinet_lkxmne_2)_1',
                    'close(top_cabinet_lkxmne_2)_1']

    file_name = "can_meat_1748934139397589"
    with open(os.path.join(os.path.join(root_path, file_name), 'action_sequence.pkl'), 'wb') as f:
        pickle.dump(correct_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"file {file_name} has been corrected")

    # putting up Christmas decorations inside

    correct_list= ['navigate_to(floors_uzsntg_0)_1',
                   'grasp(wicker_basket_218)_1',
                   'navigate_to(coffee_table_rlsebe_0)_1',
                   'place_ontop(wicker_basket_218, coffee_table_rlsebe_0)_1',
                   'navigate_to(sofa_lugrhk_1)_1',
                   'grasp(pillar_candle_222)_1',
                   'navigate_to(breakfast_table_rhjoby_0)_1',
                   'place_ontop(pillar_candle_222, breakfast_table_rhjoby_0)_1',
                   'navigate_to(sofa_lugrhk_1)_2',
                   'grasp(pillar_candle_223)_1',
                   'navigate_to(breakfast_table_rhjoby_0)_2',
                   'place_ontop(pillar_candle_223, breakfast_table_rhjoby_0)_1',
                   'navigate_to(sofa_lugrhk_1)_3',
                   'grasp(candy_cane_224)_1',
                   'navigate_to(breakfast_table_rhjoby_0)_3',
                   'place_ontop(candy_cane_224, breakfast_table_rhjoby_0)_1',
                   'navigate_to(gift_box_219)_1', 'grasp(gift_box_219)_1', 'navigate_to(christmas_tree_228)_1', 'place_under(gift_box_219, christmas_tree_228)_1',
                   'navigate_to(gift_box_220)_1', 'grasp(gift_box_220)_1', 'navigate_to(christmas_tree_228)_2', 'place_under(gift_box_220, christmas_tree_228)_1',
                   'navigate_to(gift_box_221)_1', 'grasp(gift_box_221)_1', 'navigate_to(christmas_tree_228)_3', 'place_under(gift_box_221, christmas_tree_228)_1']

    file_name = "putting_up_Christmas_decorations_inside_1752574067758371"
    with open(os.path.join(os.path.join(root_path, file_name), 'action_sequence.pkl'), 'wb') as f:
        pickle.dump(correct_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"file {file_name} has been corrected")

    #sorting vegetables
    correct_list = ['navigate_to(wicker_basket_221)_1', 'grasp(wicker_basket_221)_1',  'navigate_to(countertop_kelzer_0)_1',
                    'grasp(sweet_corn_213)_1','place_inside(sweet_corn_213, mixing_bowl_223)_1',
                    'grasp(sweet_corn_211)_1',
                    'place_inside(sweet_corn_211, mixing_bowl_223)_1',
                    'grasp(sweet_corn_212)_1',
                    'place_inside(sweet_corn_212, mixing_bowl_223)_1',
                    'place_onfloor(wicker_basket_221,floors_kxcpgy_0)',
                    'navigate_to(wicker_basket_221)_2',
                    'grasp(wicker_basket_221)_2',
                    'navigate_to(mixing_bowl_222)_1',
                    'grasp(bok_choy_217)_1', 'place_inside(bok_choy_217, mixing_bowl_222)_1',
                    'grasp(bok_choy_219)_1', 'place_inside(bok_choy_219, mixing_bowl_222)_1',
                    'grasp(bok_choy_218)_1', 'place_inside(bok_choy_218, mixing_bowl_222)_1',
                    'place_onfloor(wicker_basket_221, floors_kxcpgy_0)_1',
                    'navigate_to(wicker_basket_220)_1', 'grasp(wicker_basket_220)_1',
                    'navigate_to(countertop_kelzer_0)_2',
                    'grasp(vidalia_onion_214)_1'
                    'place_inside(vidalia_onion_214, mixing_bowl_222)_1',
                    'grasp(vidalia_onion_215)_1',
                    'place_inside(vidalia_onion_215, mixing_bowl_222)_1',
                    'grasp(broccoli_210)_1',
                    'place_inside(broccoli_210, mixing_bowl_224)_1',
                    'grasp(broccoli_209)_1',
                    'place_inside(broccoli_209, mixing_bowl_224)_1',
                    'grasp(leek_207)_1', 'place_inside(leek_207, mixing_bowl_224)_1',
                    'grasp(leek_208)_1', 'place_inside(leek_208, mixing_bowl_224)_1',
                    'place_onfloor(wicker_basket_220, floors_kxcpgy_0)_1']

    file_name = 'sorting_vegetables_1753928918914038'
    with open(os.path.join(os.path.join(root_path, file_name), 'action_sequence.pkl'), 'wb') as f:
        pickle.dump(correct_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"file {file_name} has been corrected")

    # wash dog toys
    correct_list = ['navigate_to(washer_ynwamu_0)_1', 'open(washer_ynwamu_0)_1', 'navigate_to(bottom_cabinet_no_top_gjrero_0)_1', 'open(bottom_cabinet_no_top_gjrero_0)_1', 'grasp(teddy_bear_191)_1', 'grasp(teddy_bear_190)_1', 'navigate_to(washer_ynwamu_0)_2', 'place_inside(teddy_bear_191, washer_ynwamu_0)_1', 'place_inside(teddy_bear_190, washer_ynwamu_0)_1', 'navigate_to(bottom_cabinet_no_top_gjrero_0)_2', 'grasp(softball_188)_1', 'grasp(tennis_ball_189)_1', 'navigate_to(washer_ynwamu_0)_3', 'place_inside(softball_188, washer_ynwamu_0)_1', 'place_inside(tennis_ball_189, washer_ynwamu_0)_1', 'close(washer_ynwamu_0)_1', 'toggle_on(washer_ynwamu_0)_1']

    file_name = 'wash_dog_toys_1751858242498986'
    with open(os.path.join(os.path.join(root_path, file_name), 'action_sequence.pkl'), 'wb') as f:
        pickle.dump(correct_list, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"file {file_name} has been corrected")

    # file_name = 'putting_up_Christmas_decorations_inside_1752574067758371'
    #
    # file_path = os.path.join(root_path, file_name)
    # action_list_file_path = os.path.join(file_path, 'action_sequence.pkl')
    #
    # with open(action_list_file_path, 'rb') as file:
    #     # Use pickle.load() to read the list from the file
    #     loaded_list = pickle.load(file)
    # parts = re.split(r'(?=\d)', file_name, maxsplit=1)
    # task_name = parts[0].replace('_', ' ').rstrip()
    # print(task_name)
    # print("================================================================================================================")
    # print(loaded_list)
    # print("================================================================================================================")
