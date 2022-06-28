\ Model (null)_copy
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x_0 + x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_7 + x_8 + x_9 + x_10 + x_11
   + x_12 + x_13 + x_14 + x_15 + x_16 + x_17 + x_18 + x_19 + x_20 + x_21
   + x_22 + x_23 + x_24 + x_25 + x_26 + x_27 + x_28 + x_29 + x_30 + x_31
   + x_32 + x_33 + x_34 + x_35 + x_36 + x_37 + x_38 + x_39 + x_40 + x_41
   + x_42 + x_43 + x_44 + x_45 + x_46 + x_47 + x_48 + x_49 + x_50 + x_51
   + x_52 + x_53 + x_54 + x_55 + x_56 + x_57 + x_58 + x_59 + x_60 + x_61
   + x_62 + x_63 + x_64 + x_65 + x_66 + x_67 + x_68 + x_69 + x_70 + z_0
   + z_1
Subject To
 z_0_def: 2.1 x_0 + 0.9 x_1 - 0.9 x_2 + x_8 + x_70 - z_0 = 150
 z_1_def: - x_0 - z_1 = -100
 commonCons_0: x_8 <= 100
 commonCons_1: - x_0 - x_1 + x_2 <= 0
 commonCons_2: - 0.9 x_0 - 0.9 x_1 + 0.9 x_2 <= -52.5
 commonCons_3: - x_1 + x_3 + x_4 + x_5 + x_6 <= 0
 commonCons_4: x_1 - x_3 - x_4 - x_5 - x_6 <= 0
 uv_sum_0: u_0 + v_0 = 1
 uv_sum_1: u_1 + v_1 = 1
 z_ind_0_L_Mu_0: u_0 = 1 -> z_0 <= 0
 x_ind_0_L_MuDash_0: v_0 = 1 -> x_0 <= 0
 z_ind_1_L_Mu_1: u_1 = 1 -> z_1 <= 0
 x_ind_1_L_MuDash_1: v_1 = 1 -> x_70 <= 0
Bounds
Binaries
 u_0 u_1 v_0 v_1
End
