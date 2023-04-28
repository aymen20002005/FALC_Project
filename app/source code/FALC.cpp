#include "FALC.h"
#include <QProcess>
#include<QDebug>
#include<Qdir>
#include<QMessageBox>
#include <QRegularExpression>
#include <QString>
#include <QStringList>

FALC::FALC(QWidget* parent)
    : QMainWindow(parent)
{
    ui.setupUi(this);
    QFont font("Segoe UI", 10);
    QSize iconSize(32, 32);

    QFont font2("Arial", 14);
    ui.falc->setFont(font2);
    ui.comp_french->setFont(font2);




    connect(ui.trad, &QPushButton::clicked, this, &FALC::traduire);
    ui.trad->setFont(font);
    QIcon icon1("assets/trad.png");
    ui.trad->setIconSize(iconSize);
    ui.trad->setIcon(icon1.pixmap(iconSize));

    connect(ui.set, &QPushButton::clicked, this, &FALC::set);
    ui.set->setFont(font);
    QIcon icon2("assets/set.png");
    ui.set->setIconSize(iconSize);
    ui.set->setIcon(icon2.pixmap(iconSize));

    QAction* aProposAction = new QAction(tr("A propos"), this);
    menuBar()->addAction(aProposAction);
    connect(aProposAction, &QAction::triggered, this, &FALC::showAboutDialog);
}

FALC::~FALC()
{
}

void FALC::traduire()
{
    ui.falc->clear();
    QString inputText = ui.comp_french->toPlainText();
    QProcess* process = new QProcess(this);

    connect(process, &QProcess::readyReadStandardOutput, this, [=]() {
        QString output = process->readAllStandardOutput();
    qDebug() << "out: " << output;
 
    ui.falc->insertPlainText(output);
        });

    connect(process, &QProcess::readyReadStandardError, this, [=]() {
        QString error = process->readAllStandardError();
    qDebug() << "error: " << error;
    ui.falc->insertPlainText(error);
        });

    QString currentDir = QDir::currentPath();
    process->setWorkingDirectory(currentDir);
    QString scriptPath = QCoreApplication::applicationDirPath() + "/script.py";
    process->start("python", QStringList() << scriptPath << inputText);
    qDebug() << "started";
    QMessageBox::information(this, "Veuillez patienter", "L'execution va prendre quelques secondes. Si c'est votre premiere execution, cela prendra probablement plus de temps.");


}



void FALC::showAboutDialog()
{
    QMessageBox::information(this, tr("About"), tr("Projet FALC 2022/2023 -- ENSTA PARIS."));
}

void FALC::set()
{
    QProcess* process = new QProcess(this);
    QString currentDir = QDir::currentPath();
    process->setWorkingDirectory(currentDir);
    connect(process, &QProcess::readyReadStandardOutput, this, [=]() {
        QString output = process->readAllStandardOutput();
    qDebug() << "out: " << output;
    ui.falc->insertPlainText(output);
        });
    process->start("pip", QStringList() << "install" << "--upgrade" << "torch" << "transformers" << "sentencepiece");
    process->waitForFinished();
    QMessageBox::information(this, "Succes !", "Vous pouvez maintenant commencer a utiliser l'application.");

}