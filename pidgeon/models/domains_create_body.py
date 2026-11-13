from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainsCreateBody")


@_attrs_define
class DomainsCreateBody:
    """
    Attributes:
        domain (str): A domain name you own, or the shared one. An alternative to `domain_id`.
        inbound_enabled (bool | Unset):
        pod_id (UUID | Unset): The pod this domain sends from, for one of your customers. Leave it out for the default
            pod; a pod key’s domain always goes in its own pod.
    """

    domain: str
    inbound_enabled: bool | Unset = UNSET
    pod_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        inbound_enabled = self.inbound_enabled

        pod_id: str | Unset = UNSET
        if not isinstance(self.pod_id, Unset):
            pod_id = str(self.pod_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "domain": domain,
            }
        )
        if inbound_enabled is not UNSET:
            field_dict["inbound_enabled"] = inbound_enabled
        if pod_id is not UNSET:
            field_dict["pod_id"] = pod_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        inbound_enabled = d.pop("inbound_enabled", UNSET)

        _pod_id = d.pop("pod_id", UNSET)
        pod_id: UUID | Unset
        if isinstance(_pod_id, Unset):
            pod_id = UNSET
        else:
            pod_id = UUID(_pod_id)

        domains_create_body = cls(
            domain=domain,
            inbound_enabled=inbound_enabled,
            pod_id=pod_id,
        )

        return domains_create_body
