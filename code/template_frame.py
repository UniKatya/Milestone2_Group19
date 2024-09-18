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
import wx.grid

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
		self.m_notebook1.AddPage( self.m_panelHome, u"Home", False )
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

		self.m_gridRangeFilter = wx.grid.Grid( self.m_panelRangeFilter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_gridRangeFilter.CreateGrid( 5, 5 )
		self.m_gridRangeFilter.EnableEditing( True )
		self.m_gridRangeFilter.EnableGridLines( True )
		self.m_gridRangeFilter.EnableDragGridSize( False )
		self.m_gridRangeFilter.SetMargins( 0, 0 )

		# Columns
		self.m_gridRangeFilter.EnableDragColMove( False )
		self.m_gridRangeFilter.EnableDragColSize( True )
		self.m_gridRangeFilter.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_gridRangeFilter.EnableDragRowSize( True )
		self.m_gridRangeFilter.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_gridRangeFilter.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizerRangeMain.Add( self.m_gridRangeFilter, 0, wx.ALL, 5 )


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

		self.m_gridLevelFilter = wx.grid.Grid( self.m_panelLevelFilter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_gridLevelFilter.CreateGrid( 5, 5 )
		self.m_gridLevelFilter.EnableEditing( True )
		self.m_gridLevelFilter.EnableGridLines( True )
		self.m_gridLevelFilter.EnableDragGridSize( False )
		self.m_gridLevelFilter.SetMargins( 0, 0 )

		# Columns
		self.m_gridLevelFilter.EnableDragColMove( False )
		self.m_gridLevelFilter.EnableDragColSize( True )
		self.m_gridLevelFilter.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_gridLevelFilter.EnableDragRowSize( True )
		self.m_gridLevelFilter.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_gridLevelFilter.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizerLevelFilter.Add( self.m_gridLevelFilter, 0, wx.ALL, 5 )


		self.m_panelLevelFilter.SetSizer( bSizerLevelFilter )
		self.m_panelLevelFilter.Layout()
		bSizerLevelFilter.Fit( self.m_panelLevelFilter )
		self.m_notebook1.AddPage( self.m_panelLevelFilter, u"Level Filter", False )
		self.m_panelMealPlanner = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel27 = wx.Panel( self.m_panelMealPlanner, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel28 = wx.Panel( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer44 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText42 = wx.StaticText( self.m_panel28, wx.ID_ANY, u"Daily Calories:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		bSizer44.Add( self.m_staticText42, 0, wx.ALL, 5 )


		bSizer43.Add( bSizer44, 1, wx.EXPAND, 5 )

		bSizer45 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText38 = wx.StaticText( self.m_panel28, wx.ID_ANY, u"xxxx", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		bSizer45.Add( self.m_staticText38, 0, wx.ALL, 5 )


		bSizer43.Add( bSizer45, 1, wx.EXPAND, 5 )


		fgSizer7.Add( bSizer43, 1, wx.EXPAND, 5 )


		fgSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText39 = wx.StaticText( self.m_panel28, wx.ID_ANY, u"Food Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		bSizer41.Add( self.m_staticText39, 0, wx.ALL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self.m_panel28, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_textCtrl9, 0, wx.ALL, 5 )


		fgSizer7.Add( bSizer41, 1, wx.EXPAND, 5 )


		fgSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer40 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText41 = wx.StaticText( self.m_panel28, wx.ID_ANY, u"Quantity:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		bSizer40.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self.m_panel28, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer40.Add( self.m_textCtrl8, 0, wx.ALL, 5 )


		fgSizer7.Add( bSizer40, 1, wx.EXPAND, 5 )

		self.m_button7 = wx.Button( self.m_panel28, wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel28.SetSizer( fgSizer7 )
		self.m_panel28.Layout()
		fgSizer7.Fit( self.m_panel28 )
		bSizer23.Add( self.m_panel28, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel30 = wx.Panel( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel30.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer49 = wx.BoxSizer( wx.VERTICAL )


		bSizer49.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText19 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Food Details:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		bSizer49.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText43 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Food", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		bSizer49.Add( self.m_staticText43, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText47 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Quantity", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		bSizer49.Add( self.m_staticText47, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText44 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"xxxx calories", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		bSizer49.Add( self.m_staticText44, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button8 = wx.Button( self.m_panel30, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer49.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer49.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel30.SetSizer( bSizer49 )
		self.m_panel30.Layout()
		bSizer49.Fit( self.m_panel30 )
		bSizer23.Add( self.m_panel30, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel27.SetSizer( bSizer23 )
		self.m_panel27.Layout()
		bSizer23.Fit( self.m_panel27 )
		bSizer22.Add( self.m_panel27, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel31 = wx.Panel( self.m_panelMealPlanner, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel31.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer57 = wx.BoxSizer( wx.VERTICAL )


		bSizer57.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText31 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"MEAL PLANNER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		bSizer57.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )


		bSizer57.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText18 = wx.StaticText( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer57.Add( self.m_staticText18, 0, wx.ALL, 5 )

		bSizer72 = wx.BoxSizer( wx.VERTICAL )

		gSizer18 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer76 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid1 = wx.grid.Grid( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 5, 5 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.SetRowSize( 0, 19 )
		self.m_grid1.SetRowSize( 1, 19 )
		self.m_grid1.SetRowSize( 2, 19 )
		self.m_grid1.SetRowSize( 3, 19 )
		self.m_grid1.SetRowSize( 4, 19 )
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.m_grid1.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer76.Add( self.m_grid1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer18.Add( bSizer76, 1, wx.EXPAND, 5 )

		bSizer75 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText46 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Enter a name to look at food details:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		bSizer75.Add( self.m_staticText46, 0, wx.ALL, 0 )

		self.m_textCtrl10 = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer75.Add( self.m_textCtrl10, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self.m_panel31, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer75.Add( self.m_button9, 0, wx.ALL, 5 )


		gSizer18.Add( bSizer75, 1, wx.EXPAND, 5 )


		bSizer72.Add( gSizer18, 1, wx.EXPAND, 5 )


		bSizer57.Add( bSizer72, 1, wx.EXPAND, 5 )


		self.m_panel31.SetSizer( bSizer57 )
		self.m_panel31.Layout()
		bSizer57.Fit( self.m_panel31 )
		bSizer22.Add( self.m_panel31, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panelMealPlanner.SetSizer( bSizer22 )
		self.m_panelMealPlanner.Layout()
		bSizer22.Fit( self.m_panelMealPlanner )
		self.m_notebook1.AddPage( self.m_panelMealPlanner, u"Meal Planner", True )

		bSizer2.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 0 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 0 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonSearch.Bind( wx.EVT_BUTTON, self.display_nutritional_info )
		self.m_buttonBreakdown.Bind( wx.EVT_BUTTON, self.display_charts )
		self.m_button7.Bind( wx.EVT_BUTTON, self.display_meal_plan )
		self.m_button8.Bind( wx.EVT_BUTTON, self.remove_food_from_meal_plan )
		self.m_button9.Bind( wx.EVT_BUTTON, self.display_food )

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

	def display_food( self, event ):
		event.Skip()


