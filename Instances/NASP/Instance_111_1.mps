NAME (null)_copy
ROWS
 N  OBJ
 E  z_0_def 
 E  z_1_def 
 L  commonCons_0
 L  commonCons_1
 L  commonCons_2
 L  commonCons_3
 L  commonCons_4
 E  uv_sum_0
 E  uv_sum_1
 L  z_ind_0_L_Mu_0
 L  x_ind_0_L_MuDash_0
 L  z_ind_1_L_Mu_1
 L  x_ind_1_L_MuDash_1
COLUMNS
    x_0       OBJ       1
    x_0       z_0_def   1.5
    x_0       z_1_def   -1
    x_0       commonCons_1  -1
    x_0       commonCons_2  -0.7
    x_0       x_ind_0_L_MuDash_0  1
    x_1       OBJ       1
    x_1       z_0_def   0.7
    x_1       commonCons_1  -1
    x_1       commonCons_2  -0.7
    x_1       commonCons_3  -1
    x_1       commonCons_4  1
    x_2       OBJ       1
    x_2       z_0_def   -0.7
    x_2       commonCons_1  1
    x_2       commonCons_2  0.7
    x_3       OBJ       1
    x_3       commonCons_3  1
    x_3       commonCons_4  -1
    x_4       OBJ       1
    x_4       commonCons_3  1
    x_4       commonCons_4  -1
    x_5       OBJ       1
    x_5       commonCons_3  1
    x_5       commonCons_4  -1
    x_6       OBJ       1
    x_6       commonCons_3  1
    x_6       commonCons_4  -1
    x_7       OBJ       1
    x_8       OBJ       1
    x_8       z_0_def   1
    x_8       commonCons_0  1
    x_9       OBJ       1
    x_10      OBJ       1
    x_11      OBJ       1
    x_12      OBJ       1
    x_13      OBJ       1
    x_14      OBJ       1
    x_15      OBJ       1
    x_16      OBJ       1
    x_17      OBJ       1
    x_18      OBJ       1
    x_19      OBJ       1
    x_20      OBJ       1
    x_21      OBJ       1
    x_22      OBJ       1
    x_23      OBJ       1
    x_24      OBJ       1
    x_25      OBJ       1
    x_26      OBJ       1
    x_27      OBJ       1
    x_28      OBJ       1
    x_29      OBJ       1
    x_30      OBJ       1
    x_31      OBJ       1
    x_32      OBJ       1
    x_33      OBJ       1
    x_34      OBJ       1
    x_35      OBJ       1
    x_36      OBJ       1
    x_37      OBJ       1
    x_38      OBJ       1
    x_39      OBJ       1
    x_40      OBJ       1
    x_41      OBJ       1
    x_42      OBJ       1
    x_43      OBJ       1
    x_44      OBJ       1
    x_45      OBJ       1
    x_46      OBJ       1
    x_47      OBJ       1
    x_48      OBJ       1
    x_49      OBJ       1
    x_50      OBJ       1
    x_51      OBJ       1
    x_52      OBJ       1
    x_53      OBJ       1
    x_54      OBJ       1
    x_55      OBJ       1
    x_56      OBJ       1
    x_57      OBJ       1
    x_58      OBJ       1
    x_59      OBJ       1
    x_60      OBJ       1
    x_61      OBJ       1
    x_62      OBJ       1
    x_63      OBJ       1
    x_64      OBJ       1
    x_65      OBJ       1
    x_66      OBJ       1
    x_67      OBJ       1
    x_68      OBJ       1
    x_69      OBJ       1
    x_70      OBJ       1
    x_71      OBJ       1
    x_72      OBJ       1
    x_73      OBJ       1
    x_74      OBJ       1
    x_74      z_0_def   1
    x_74      x_ind_1_L_MuDash_1  1
    z_0       OBJ       1
    z_0       z_0_def   -1
    z_0       z_ind_0_L_Mu_0  1
    z_1       OBJ       1
    z_1       z_1_def   -1
    z_1       z_ind_1_L_Mu_1  1
    MARKER    'MARKER'                 'INTORG'
    u_0       uv_sum_0  1
    u_1       uv_sum_1  1
    v_0       uv_sum_0  1
    v_1       uv_sum_1  1
    MARKER    'MARKER'                 'INTEND'
RHS
    RHS1      z_0_def   100
    RHS1      z_1_def   -1000
    RHS1      commonCons_0  100
    RHS1      commonCons_2  -70
    RHS1      uv_sum_0  1
    RHS1      uv_sum_1  1
    RHS1      z_ind_0_L_Mu_0  0
    RHS1      x_ind_0_L_MuDash_0  0
    RHS1      z_ind_1_L_Mu_1  0
    RHS1      x_ind_1_L_MuDash_1  0
BOUNDS
 BV BND1      u_0     
 BV BND1      u_1     
 BV BND1      v_0     
 BV BND1      v_1     
INDICATORS
 IF z_ind_0_L_Mu_0  u_0       1
 IF x_ind_0_L_MuDash_0  v_0       1
 IF z_ind_1_L_Mu_1  u_1       1
 IF x_ind_1_L_MuDash_1  v_1       1
ENDATA
