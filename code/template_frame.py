# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Nutrition Database", pos = wx.DefaultPosition, size = wx.Size( 683,442 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebook1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_notebook1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		self.m_panelHome = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer7 = wx.GridSizer( 1, 1, 0, 0 )

		self.m_richText6 = wx.richtext.RichTextCtrl( self.m_panelHome, wx.ID_ANY, u"Search Food : Allows for the user to search for a food by name through an input box. \nThe system will then provide the food and it's nutritional information.\n\nNutritional Breakdown : Allows for the user to view nutritional breakdown through a bar graph and pie chart of their selected food item.\n\nRange Filter: Allows for the user to filter a list of foods through the range they give into the system. The system will then filter and return a list of foods that fit inside of this range.\n\nLevel Filter : Allows for the user to filter food through entering content levels (low, medium, high) for their chosen nutrient such as protein or fats.\n\nMeal Planner : Allows for the user to create a meal plan by selecting a food and the quantity which the system will then calculate and add to the meal plan.\n\n\n", wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		gSizer7.Add( self.m_richText6, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panelHome.SetSizer( gSizer7 )
		self.m_panelHome.Layout()
		gSizer7.Fit( self.m_panelHome )
		self.m_notebook1.AddPage( self.m_panelHome, u"Home", True )
		self.m_panelSearch = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizerSearchFrame = wx.BoxSizer( wx.VERTICAL )

		bSizerSearchTop = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticTextSearch = wx.StaticText( self.m_panelSearch, wx.ID_ANY, u"Food Name :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSearch.Wrap( -1 )

		bSizerSearchTop.Add( self.m_staticTextSearch, 0, wx.ALL, 8 )

		self.m_textCtrlSearch = wx.TextCtrl( self.m_panelSearch, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlSearch.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizerSearchTop.Add( self.m_textCtrlSearch, 0, wx.ALL, 5 )

		self.m_buttonSearch = wx.Button( self.m_panelSearch, wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonSearch.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_buttonSearch.SetMaxSize( wx.Size( 50,-1 ) )

		bSizerSearchTop.Add( self.m_buttonSearch, 0, wx.ALL, 5 )


		bSizerSearchFrame.Add( bSizerSearchTop, 0, wx.EXPAND|wx.TOP, 10 )

		bSizerSearchBottom = wx.BoxSizer( wx.VERTICAL )

		self.m_staticTextTitle = wx.StaticText( self.m_panelSearch, wx.ID_ANY, u"Please enter a food name", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticTextTitle.Wrap( -1 )

		bSizerSearchBottom.Add( self.m_staticTextTitle, 0, wx.ALL, 8 )

		self.m_richText2 = wx.richtext.RichTextCtrl( self.m_panelSearch, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizerSearchBottom.Add( self.m_richText2, 1, wx.EXPAND |wx.ALL, 5 )


		bSizerSearchFrame.Add( bSizerSearchBottom, 1, wx.EXPAND|wx.TOP, 10 )


		self.m_panelSearch.SetSizer( bSizerSearchFrame )
		self.m_panelSearch.Layout()
		bSizerSearchFrame.Fit( self.m_panelSearch )
		self.m_notebook1.AddPage( self.m_panelSearch, u"Search", False )
		self.m_panelBreakdown = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizerBreakdownFrame = wx.BoxSizer( wx.VERTICAL )

		bSizerBreakdownTop = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticTextBreakdownSearch = wx.StaticText( self.m_panelBreakdown, wx.ID_ANY, u"Food Name :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextBreakdownSearch.Wrap( -1 )

		bSizerBreakdownTop.Add( self.m_staticTextBreakdownSearch, 0, wx.ALL, 8 )

		self.m_textCtrl3 = wx.TextCtrl( self.m_panelBreakdown, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerBreakdownTop.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_buttonBreakdown = wx.Button( self.m_panelBreakdown, wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonBreakdown.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_buttonBreakdown.SetMaxSize( wx.Size( 50,-1 ) )

		bSizerBreakdownTop.Add( self.m_buttonBreakdown, 0, wx.ALL, 5 )


		bSizerBreakdownFrame.Add( bSizerBreakdownTop, 0, wx.EXPAND|wx.TOP, 10 )

		bSizer281 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText58 = wx.StaticText( self.m_panelBreakdown, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )

		bSizer281.Add( self.m_staticText58, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panelFoodInfo = wx.Panel( self.m_panelBreakdown, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer281.Add( self.m_panelFoodInfo, 1, wx.EXPAND |wx.ALL, 5 )


		bSizerBreakdownFrame.Add( bSizer281, 1, wx.EXPAND, 5 )


		self.m_panelBreakdown.SetSizer( bSizerBreakdownFrame )
		self.m_panelBreakdown.Layout()
		bSizerBreakdownFrame.Fit( self.m_panelBreakdown )
		self.m_notebook1.AddPage( self.m_panelBreakdown, u"Nutritional Breakdown", False )
		self.m_panelRangeFilter = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizerRangeMain = wx.BoxSizer( wx.VERTICAL )

		bSizerRangeTop = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticTextSelectNutrientFilter = wx.StaticText( self.m_panelRangeFilter, wx.ID_ANY, u"Select Nutrient :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSelectNutrientFilter.Wrap( -1 )

		bSizerRangeTop.Add( self.m_staticTextSelectNutrientFilter, 0, wx.ALL, 8 )

		m_choiceNutrientRangeChoices = [ u"Fat", u"Saturated Fats", u"Monounsaturated Fats", u"Polyunsaturated Fats", u"Carbohydrates", u"Sugars", u"Protein", u"Dietary Fiber", u"Cholesterol", u"Sodium", u"Water", u"Vitamin A", u"Vitamin B1", u"Vitamin B11", u"Vitamin B12", u"Vitamin B2", u"Vitamin B3", u"Vitamin B5", u"Vitamin B6", u"Vitamin C", u"Vitamin D", u"Vitamin E", u"Vitamin K", u"Calcium", u"Copper", u"Iron", u"Magnesium", u"Manganese", u"Phosphorus", u"Potassium", u"Selenium", u"Zinc", wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString ]
		self.m_choiceNutrientRange = wx.Choice( self.m_panelRangeFilter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceNutrientRangeChoices, 0 )
		self.m_choiceNutrientRange.SetSelection( 0 )
		self.m_choiceNutrientRange.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_choiceNutrientRange.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizerRangeTop.Add( self.m_choiceNutrientRange, 0, wx.ALL, 5 )

		self.m_staticTextMin = wx.StaticText( self.m_panelRangeFilter, wx.ID_ANY, u"Min:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMin.Wrap( -1 )

		bSizerRangeTop.Add( self.m_staticTextMin, 0, wx.ALL, 5 )

		self.m_textCtrlMinVal = wx.TextCtrl( self.m_panelRangeFilter, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlMinVal.SetMaxSize( wx.Size( 50,-1 ) )

		bSizerRangeTop.Add( self.m_textCtrlMinVal, 0, wx.ALL, 5 )

		self.m_staticTextMax = wx.StaticText( self.m_panelRangeFilter, wx.ID_ANY, u"Max:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMax.Wrap( -1 )

		bSizerRangeTop.Add( self.m_staticTextMax, 0, wx.ALL, 5 )

		self.m_textCtrlMaxVal = wx.TextCtrl( self.m_panelRangeFilter, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlMaxVal.SetMaxSize( wx.Size( 50,-1 ) )

		bSizerRangeTop.Add( self.m_textCtrlMaxVal, 0, wx.ALL, 5 )

		self.m_buttonRangeSearch = wx.Button( self.m_panelRangeFilter, wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonRangeSearch.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_buttonRangeSearch.SetMaxSize( wx.Size( 50,-1 ) )

		bSizerRangeTop.Add( self.m_buttonRangeSearch, 0, wx.ALL, 5 )


		bSizerRangeMain.Add( bSizerRangeTop, 0, wx.EXPAND|wx.TOP, 10 )

		bSizerRangeBottom = wx.BoxSizer( wx.VERTICAL )

		self.m_panelRangeList = wx.Panel( self.m_panelRangeFilter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizerRangeBottom.Add( self.m_panelRangeList, 1, wx.EXPAND |wx.ALL, 5 )


		bSizerRangeMain.Add( bSizerRangeBottom, 1, wx.EXPAND, 5 )


		self.m_panelRangeFilter.SetSizer( bSizerRangeMain )
		self.m_panelRangeFilter.Layout()
		bSizerRangeMain.Fit( self.m_panelRangeFilter )
		self.m_notebook1.AddPage( self.m_panelRangeFilter, u"Range Filter", False )
		self.m_panelLevelFilter = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizerLevelFilter = wx.BoxSizer( wx.VERTICAL )

		bSizerFilterTop = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticTextSelectNutrientLevel = wx.StaticText( self.m_panelLevelFilter, wx.ID_ANY, u"Select Nutrient :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSelectNutrientLevel.Wrap( -1 )

		self.m_staticTextSelectNutrientLevel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, wx.EmptyString ) )

		bSizerFilterTop.Add( self.m_staticTextSelectNutrientLevel, 0, wx.ALL, 8 )

		m_choiceNutrientLevelChoices = [ u"Fat", u"Saturated Fats", u"Monounsaturated Fats", u"Polyunsaturated Fats", u"Carbohydrates", u"Sugars", u"Protein", u"Dietary Fiber", u"Cholesterol", u"Sodium", u"Water", u"Vitamin A", u"Vitamin B1", u"Vitamin B11", u"Vitamin B12", u"Vitamin B2", u"Vitamin B3", u"Vitamin B5", u"Vitamin B6", u"Vitamin C", u"Vitamin D", u"Vitamin E", u"Vitamin K", u"Calcium", u"Copper", u"Iron", u"Magnesium", u"Manganese", u"Phosphorus", u"Potassium", u"Selenium", u"Zinc", wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString ]
		self.m_choiceNutrientLevel = wx.Choice( self.m_panelLevelFilter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceNutrientLevelChoices, 0 )
		self.m_choiceNutrientLevel.SetSelection( 0 )
		self.m_choiceNutrientLevel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_choiceNutrientLevel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_choiceNutrientLevel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizerFilterTop.Add( self.m_choiceNutrientLevel, 0, wx.ALL, 5 )

		self.m_radioBtnLow = wx.RadioButton( self.m_panelLevelFilter, wx.ID_ANY, u"Low", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerFilterTop.Add( self.m_radioBtnLow, 0, wx.ALL, 8 )

		self.m_radioBtnMedium = wx.RadioButton( self.m_panelLevelFilter, wx.ID_ANY, u"Medium", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerFilterTop.Add( self.m_radioBtnMedium, 0, wx.ALL, 8 )

		self.m_radioBtnHigh = wx.RadioButton( self.m_panelLevelFilter, wx.ID_ANY, u"High", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerFilterTop.Add( self.m_radioBtnHigh, 0, wx.ALL, 8 )

		self.m_buttonLevelSearch = wx.Button( self.m_panelLevelFilter, wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonLevelSearch.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_buttonLevelSearch.SetMaxSize( wx.Size( 50,-1 ) )

		bSizerFilterTop.Add( self.m_buttonLevelSearch, 0, wx.ALL, 5 )


		bSizerLevelFilter.Add( bSizerFilterTop, 0, wx.EXPAND|wx.TOP, 10 )

		bSizerFilterBottom = wx.BoxSizer( wx.VERTICAL )

		self.m_panelLevelList = wx.Panel( self.m_panelLevelFilter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panelLevelList.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizerFilterBottom.Add( self.m_panelLevelList, 1, wx.EXPAND |wx.ALL, 0 )


		bSizerLevelFilter.Add( bSizerFilterBottom, 1, wx.EXPAND|wx.TOP, 10 )


		self.m_panelLevelFilter.SetSizer( bSizerLevelFilter )
		self.m_panelLevelFilter.Layout()
		bSizerLevelFilter.Fit( self.m_panelLevelFilter )
		self.m_notebook1.AddPage( self.m_panelLevelFilter, u"Level Filter", False )
		self.m_panelMealPlanner = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizerPlanner = wx.GridSizer( 2, 2, 0, 0 )

		self.m_panel13 = wx.Panel( self.m_panelMealPlanner, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel13.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizerPlanner = wx.FlexGridSizer( 3, 3, 0, 0 )
		fgSizerPlanner.SetFlexibleDirection( wx.BOTH )
		fgSizerPlanner.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticTextCalories = wx.StaticText( self.m_panel13, wx.ID_ANY, u"Daily Calories :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCalories.Wrap( -1 )

		fgSizerPlanner.Add( self.m_staticTextCalories, 0, wx.ALL, 8 )

		self.m_staticText59 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"                 xxx                              ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )

		fgSizerPlanner.Add( self.m_staticText59, 0, wx.ALL, 5 )

		bSizer282 = wx.BoxSizer( wx.VERTICAL )


		fgSizerPlanner.Add( bSizer282, 1, wx.EXPAND, 5 )

		self.m_staticTextFoodName = wx.StaticText( self.m_panel13, wx.ID_ANY, u"Food Name :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextFoodName.Wrap( -1 )

		fgSizerPlanner.Add( self.m_staticTextFoodName, 0, wx.ALL, 8 )

		self.m_textCtrl51 = wx.TextCtrl( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerPlanner.Add( self.m_textCtrl51, 0, wx.ALL, 5 )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )


		fgSizerPlanner.Add( bSizer29, 1, wx.EXPAND, 5 )

		self.m_staticTextQuantity = wx.StaticText( self.m_panel13, wx.ID_ANY, u"Quantity :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextQuantity.Wrap( -1 )

		fgSizerPlanner.Add( self.m_staticTextQuantity, 0, wx.ALL, 8 )

		self.m_textCtrl52 = wx.TextCtrl( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerPlanner.Add( self.m_textCtrl52, 0, wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_buttonMealQuantity = wx.Button( self.m_panel13, wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonMealQuantity.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_buttonMealQuantity.SetMaxSize( wx.Size( 50,-1 ) )

		bSizer30.Add( self.m_buttonMealQuantity, 0, wx.ALL, 5 )


		fgSizerPlanner.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.m_panel13.SetSizer( fgSizerPlanner )
		self.m_panel13.Layout()
		fgSizerPlanner.Fit( self.m_panel13 )
		gSizerPlanner.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panelCalories = wx.Panel( self.m_panelMealPlanner, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panelCalories.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )


		bSizer26.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticTextAddFood = wx.StaticText( self.m_panelCalories, wx.ID_ANY, u"Food : Quantity", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAddFood.Wrap( -1 )

		self.m_staticTextAddFood.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer26.Add( self.m_staticTextAddFood, 0, wx.ALIGN_CENTER|wx.ALL, 8 )

		self.m_staticTextAddCalories = wx.StaticText( self.m_panelCalories, wx.ID_ANY, u"xxxx calories", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAddCalories.Wrap( -1 )

		bSizer26.Add( self.m_staticTextAddCalories, 0, wx.ALIGN_CENTER|wx.ALL, 8 )

		self.m_buttonDelete = wx.Button( self.m_panelCalories, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonDelete.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_buttonDelete.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_buttonDelete.SetMaxSize( wx.Size( 50,-1 ) )

		bSizer26.Add( self.m_buttonDelete, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer26.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer22.Add( bSizer26, 1, wx.EXPAND|wx.TOP, 10 )


		self.m_panelCalories.SetSizer( bSizer22 )
		self.m_panelCalories.Layout()
		bSizer22.Fit( self.m_panelCalories )
		gSizerPlanner.Add( self.m_panelCalories, 1, wx.ALL|wx.EXPAND, 10 )

		self.m_panelMealPlan = wx.Panel( self.m_panelMealPlanner, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panelMealPlan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_panelMealPlan.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizerMealPlanFrame = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText60 = wx.StaticText( self.m_panelMealPlan, wx.ID_ANY, u"Meal Plan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )

		self.m_staticText60.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		bSizerMealPlanFrame.Add( self.m_staticText60, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText61 = wx.StaticText( self.m_panelMealPlan, wx.ID_ANY, u"Click the 'Show' button to view the food details.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		self.m_staticText61.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		bSizerMealPlanFrame.Add( self.m_staticText61, 0, wx.ALL, 5 )

		fgSizerMealItems = wx.FlexGridSizer( 20, 2, 0, 0 )
		fgSizerMealItems.SetFlexibleDirection( wx.BOTH )
		fgSizerMealItems.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		bSizerMealPlanFrame.Add( fgSizerMealItems, 1, wx.EXPAND, 5 )


		self.m_panelMealPlan.SetSizer( bSizerMealPlanFrame )
		self.m_panelMealPlan.Layout()
		bSizerMealPlanFrame.Fit( self.m_panelMealPlan )
		gSizerPlanner.Add( self.m_panelMealPlan, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panelMealPlanner.SetSizer( gSizerPlanner )
		self.m_panelMealPlanner.Layout()
		gSizerPlanner.Fit( self.m_panelMealPlanner )
		self.m_notebook1.AddPage( self.m_panelMealPlanner, u"Meal Planner", False )

		bSizer2.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 0 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 0 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonSearch.Bind( wx.EVT_BUTTON, self.display_nutritional_info )
		self.m_buttonBreakdown.Bind( wx.EVT_BUTTON, self.display_charts )
		self.m_buttonMealQuantity.Bind( wx.EVT_BUTTON, self.display_meal_plan )
		self.m_buttonDelete.Bind( wx.EVT_BUTTON, self.remove_food_from_meal_plan )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def display_nutritional_info( self, event ):
		event.Skip()

	def display_charts( self, event ):
		event.Skip()

	def display_meal_plan( self, event ):
		event.Skip()

	def remove_food_from_meal_plan( self, event ):
		event.Skip()


