#include "load_vehicle_interface.h"
#include "ui_load_vehicle_interface.h"

load_vehicle_interface::load_vehicle_interface(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::load_vehicle_interface)
{
    ui->setupUi(this);
}

load_vehicle_interface::~load_vehicle_interface()
{
    delete ui;
}
