import { useEffect } from "react";
import { useForm } from "react-hook-form";
import { Link as RouterLink } from "react-router-dom";
import TitleUnderline from "../../../components/TitleUnderline";
import useAsyncOptions from "../../../hooks/useAsyncOptions";
import {
  InputDate,
  InputText,
  InputSelect,
  InputAsyncSelect,
} from "../../../components/CustomInputs";
import Button from "@mui/material/Button";
import {
  email,
  composeValidators,
  alphanumeric,
  required,
  date,
  password,
} from "../../../validations";
import ButtonUi from "../../../components/UI";
import {
  InputMasterField,
  InputTextField,
  InputSelectField,
} from "../../../components/Input";
import FormFooter from "../../../components/Form/FormFooter";

export default function PagosForm({
  onSubmit,
  initialValues = {},
  isUpdating,
  urlList,
  loading,
}) {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
    control,
    reset,
  } = useForm();

  const { asyncOptions: asyncOptionsServicio } = useAsyncOptions("servicio");


  useEffect(() => {
    reset(initialValues);
  }, [initialValues]);

  return (
    <form onSubmit={handleSubmit(onSubmit)}>

<div className="w-full flex flex-wrap">

                {[
                    { type: "title", title: "Detalles del pago" },
                    { name: "descripcion", title: "Servicio a pagar" },
                    { name: "monto", title: "Pago por mes" },
                    { name: "mes", title: "Mes a pagar" },
                    { name: "total", title: "Total a pagar" },
                ].map((props, index) => {
                    return (
                        <InputMasterField
                            key={props.name || index}
                            control={control}
                            {...props}
                        />
                    );
                })}
                <div>
            </div>
            </div>
      <FormFooter {...{ loading, isUpdating, urlList }} />
      <br />
    </form>
  );
}