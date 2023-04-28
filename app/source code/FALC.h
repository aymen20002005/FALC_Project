#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_FALC.h"

class FALC : public QMainWindow
{
    Q_OBJECT

public:
    FALC(QWidget *parent = nullptr);
    ~FALC();
    void traduire();
    void showAboutDialog();
    void set();
private:
    Ui::FALCClass ui;
};
