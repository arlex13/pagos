import { Routes, Route } from "react-router-dom";
import Proyecto from "./Proyecto";
import ProyectoList from "./ProyectoList";
import NotFound from "../404";

export default function ProyectoRoutes() {
  return (
    <Routes>
      <Route path="/" element={<ProyectoList />} />
      <Route path="/create" element={<Proyecto />} />
      <Route path="/:id" element={<Proyecto />} />
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}
