\ Model (null)_copy
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x_0 + x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_7 + x_8 + x_9 + x_10 + x_11
   + x_12 + x_13 + x_14 + x_15 + x_16 + x_17 + x_18 + x_19 + x_20 + x_21
   + x_22 + x_23 + x_24 + x_25 + x_26 + x_27 + x_28 + x_29 + x_30 + x_31
   + x_32 + x_33 + x_34 + x_35 + x_36 + x_37 + x_38 + x_39 + x_40 + x_41
   + x_42 + x_43 + x_44 + x_45 + x_46 + x_47 + x_48 + x_49 + x_50 + x_51
   + z_0 + z_1 + z_2 + z_3 + z_4 + z_5
Subject To
 z_0_def: 2 x_0 + 0.9 x_1 + 0.9 x_2 + 0.9 x_3 - 0.9 x_4 + x_11 + x_49 - z_0
   = 80
 z_1_def: 0.9 x_0 + 1.9 x_1 + 0.9 x_2 + 0.9 x_3 - 0.9 x_4 + x_12 + x_50
   - z_1 = 50
 z_2_def: 0.9 x_0 + 0.9 x_1 + 2.3 x_2 + 0.9 x_3 - 0.9 x_4 + x_13 + x_51
   - z_2 = 150
 z_3_def: - x_0 - z_3 = -1000
 z_4_def: - x_1 - z_4 = -1000
 z_5_def: - x_2 - z_5 = -200
 commonCons_0: x_11 <= 300
 commonCons_1: x_12 <= 200
 commonCons_2: x_13 <= 25
 commonCons_3: - x_0 - x_1 - x_2 - x_3 + x_4 <= 0
 commonCons_4: - 0.9 x_0 - 0.9 x_1 - 0.9 x_2 - 0.9 x_3 + 0.9 x_4 <= -30
 commonCons_5: - x_3 + x_5 + x_6 + x_7 <= 0
 commonCons_6: x_3 - x_5 - x_6 - x_7 <= 0
 uv_sum_0: u_0 + v_0 = 1
 uv_sum_1: u_1 + v_1 = 1
 uv_sum_2: u_2 + v_2 = 1
 uv_sum_3: u_3 + v_3 = 1
 uv_sum_4: u_4 + v_4 = 1
 uv_sum_5: u_5 + v_5 = 1
 z_ind_0_L_Mu_0: u_0 = 1 -> z_0 <= 0
 x_ind_0_L_MuDash_0: v_0 = 1 -> x_0 <= 0
 z_ind_1_L_Mu_1: u_1 = 1 -> z_1 <= 0
 x_ind_1_L_MuDash_1: v_1 = 1 -> x_1 <= 0
 z_ind_2_L_Mu_2: u_2 = 1 -> z_2 <= 0
 x_ind_2_L_MuDash_2: v_2 = 1 -> x_2 <= 0
 z_ind_3_L_Mu_3: u_3 = 1 -> z_3 <= 0
 x_ind_3_L_MuDash_3: v_3 = 1 -> x_49 <= 0
 z_ind_4_L_Mu_4: u_4 = 1 -> z_4 <= 0
 x_ind_4_L_MuDash_4: v_4 = 1 -> x_50 <= 0
 z_ind_5_L_Mu_5: u_5 = 1 -> z_5 <= 0
 x_ind_5_L_MuDash_5: v_5 = 1 -> x_51 <= 0
Bounds
Binaries
 u_0 u_1 u_2 u_3 u_4 u_5 v_0 v_1 v_2 v_3 v_4 v_5
End
